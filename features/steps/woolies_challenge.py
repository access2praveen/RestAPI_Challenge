from behave import *
import requests, json
from datetime import datetime, timedelta
import time
import pprint

# from datetime import timedelta as td

pp = pprint.PrettyPrinter(indent=4)


@given(u'I like to surf in any 2 beaches "{Out_of_top_ten}" of Sydney')
def Search_beaches(context, Out_of_top_ten):
    context.curr_beach_name = Out_of_top_ten
    print(f"Analyzing data for beach : {Out_of_top_ten}")
    beaches = {"Bondi": 2026, "Manly": 2095, "Clovelly": 2031, "coogee": 2034, "Bronte": 2024, "Shelly": 2261,
               "Balmoral": 2088, "Nielsen Park": 2030, "Milk": 2030, "Bilgola": 2107}
    print("\n Top 10 beaches in Sydney and its POST CODE , Choose ONE \n ..............\n", beaches,"\n.................")
    time.sleep(5)


@given(u'I only like to surf on any 2 days specifically "{week_days}" in next "{total_days}" Days')
def surfing_days(context, week_days, total_days):
    context.desired_day_date = []
    week_day_index = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    #This is a list of weekdays which user is interested in
    week_days = week_days.replace('<','').replace('>','').replace(' ', '').split('&')
    #converting string to integer as feature file sends variables as string
    period = int(total_days)
    today = datetime.today()
    #iterate the dates for next 16 days 
    for i in range(0, period + 1):
        day = today + timedelta(days=i)
        # Get today's day index (For ex Monday:0 Wednesday:2)
        day_index = day.weekday()
        #Checking weather Thursday and Friday are present
        if week_day_index[day_index] in week_days:
            date = day.strftime('%Y-%m-%d')
            context.desired_day_date.append(date)
    print(f"Desired Dates {context.desired_day_date}")
   

@when(u'I look up the the weather forecast for the next 16 days using "{postcode}"')
def lookup_weather(context, postcode):
    context.curr_postcode = postcode
    endpoint_url = f"{context.url}?postal_code={postcode}&city={context.city}&key={context.apikey}"
    res = requests.get(endpoint_url)
    assert res.status_code == 200
    api_data = res.json()
    context.data = api_data["data"]
    context.api_tracker[postcode] = {'request': endpoint_url, 'response': context.data}

    for rec in context.data:
        date = rec['datetime']
        if 'weather' not in rec:
            assert False,  "Weather attribute is not available"
        if 'description' not in rec['weather']:
            assert False,  "Weather Description is not available"
        if date in context.desired_day_date:
            #print(f"Weather Description on desired {date} is {rec['weather']['description']}")
            if 'rain' not in  rec['weather']['description'].lower():
                print(f"NO RAIN FOUND on desired {date} is {rec['weather']['description']}")
                set_filter_date(context, date, 'weather_matched', 1)
                set_filter_date(context, date, 'weather_description', rec['weather']['description'])
    time.sleep(5)


@then(u'I check to if see the temperature is between "{temp_range}"')
def check_temperature(context, temp_range):
    (start_temp, end_temp) = temp_range.replace('℃','').replace('<','').replace('>','').replace(' ', '').split('and')
    #print(f"Dates for temperature between {start_temp} and {end_temp} degrees for next 16 days ")
    for rec in context.data:
        if 'temp' not in rec:
            assert False, "Temperature is not Available"

        date = rec['datetime']
        if date in context.desired_day_date:
            #print(f"Temperature on desired date {rec['datetime']} is {rec['temp']}\n")
            if rec['temp'] > int(start_temp) and rec['temp'] < int(end_temp):
                print(f"Temparature Criteria Matched on {rec['datetime']} is {rec['temp']}")
                set_filter_date(context, date, 'temp_matched', 1)
                set_filter_date(context, date, 'temp', rec['temp'])



@then(u'I check to see if UV index is <= "{uv_index}"')
def check_UV(context, uv_index):
    #print(f"Dates for UV index <= {uv_index} for next 16 days ")
    for rec in context.data:
        if 'uv' not in rec:
            assert False, "UV Index is not Available"

        date = rec['datetime']
        if date in context.desired_day_date:
            #print(f"UV Index on desired date {rec['datetime']} is {rec['uv']}\n")
            if rec['uv'] <= int(uv_index):
                print(f"UV index criteria Matched  on {rec['datetime']} is {rec['uv']}")
                set_filter_date(context, date, 'uv_matched', 1)
                set_filter_date(context, date, 'uv', rec['uv'])


@then(u'I Pick two spots based on suitable weather forecast for the day')
def Pick_Spots(context):
    # set desired spot at the end of scenario
    filter_date_obj =  context.filter_date[context.curr_postcode]
    #print("FILTER DATE OBJECT", filter_date_obj)
    for date in filter_date_obj:
        weather_descr = filter_date_obj[date]['weather_description']
        temp = filter_date_obj[date]['temp']
        uv = filter_date_obj[date]['uv']

        #if( filter_date_obj[date]['weather_matched']==1 and
        if( filter_date_obj[date]['uv_matched'] == 1
            and filter_date_obj[date]['temp_matched'] == 1):
            # all criteria matched
            print(f"Yay..Your Criteria matched for date: {date} and the Beach you should look for is {context.curr_beach_name}\n")
            if context.curr_postcode not in context.spot:
                print(context.spot)
                context.spot[context.curr_postcode] = {'beach_name':context.curr_beach_name, 'dates':[]}
            context.spot[context.curr_postcode]['dates'].append({'date': date, 'weather': weather_descr, 'temp': temp, 'uv': uv})


    print("Available SPOTS:\n")
    display_spot(context)
    # pp.pprint(context.spot)
    # pp.pprint(context.filter_date)

def set_filter_date(context, date, key, value):
    #create a datstructure and push the data into it
    if context.curr_postcode not in context.filter_date:
        context.filter_date[context.curr_postcode] = {}
    if date not in context.filter_date[context.curr_postcode]:
        context.filter_date[context.curr_postcode][date] = {
                'weather_matched': 0,
                'uv_matched': 0,
                'temp_matched': 0,
                'weather_description': 'NA',
                'temp': 'NA',
                'uv': 'NA',
        }
    context.filter_date[context.curr_postcode][date][key] = value


def display_spot(context):
    #print(context.spot)
    for postcode in context.spot.keys():
        print(f"Yay .. you should look for below dates at \n Beach Name: {context.spot[postcode]['beach_name']}, Postcode: {postcode}\n")
        for rec in context.spot[postcode]['dates']:
            print(f"\t Date: {rec['date']} - Weather: {rec['weather']}, Temp: {rec['temp']}, UV Index: {rec['uv']}\n")

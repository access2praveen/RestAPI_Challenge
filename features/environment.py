from behave.log_capture import capture
import json

def before_all(context):
    print("I m running now")
    


def before_feature(context, feature):
    print('before_feature')
    # context.desired_day_date = []
    context.filter_date = {}
    context.desired_weather_date = []
    context.spot = {}
    context.url = 'https://api.weatherbit.io/v2.0/forecast/daily'
    context.city = 'Sydney,AU'
    context.apikey = 'b3903d948a024ed395a23070d6102bb0'
    context.api_tracker = {}


def after_feature(context, feature):
    with open('api_log.json', 'w') as outfile:
        outfile.write(json.dumps(context.api_tracker, indent=2))

def before_scenario(context, scenario):
    print('test setup()')
    context.desired_day_date = []

def after_scenario(context, scenario):
    print('test cleanup()')

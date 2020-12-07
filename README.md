# RestAPI_Challenge
This script  is written on python3 using behave framework 

The Directory structure for behave framework is 

-behave.ini
-environment.py
-features\steps\code.py
-features\woolies.feature

behave.ini - File where the default command line flags are enabled

features\steps\code.py - File where the actual functions are written

features\woolies.feature - File Describes the Features, Scenario Outline , Where you can pass ( weekdays, post code, number of days) as variables

environment.py - File where the environment variables (global variables) are defined

Install below modules, if not present , else enable python virtual environment as shown below

pip install requires
pip install behave
pip install datetime 


Download the source using below command

https://github.com/access2praveen/RestAPI_Challenge

# Enable python virtual environment 

source venv\Scripts\activate 

# Run the feature using below command

behave features\woolies.feature

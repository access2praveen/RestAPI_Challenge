# RestAPI_Challenge
This script  is written on python3 using behave framework 

The Directory structure for behave framework is 

-behave.ini

-environment.py

-features\steps\code.py

-features\woolies.feature

# File Description

behave.ini - File where the default command line flags are enabled

environment.py - File where the environment variables (global variables) are defined

features\steps\code.py - File where the actual test methods are written

features\woolies.feature - File Describes the Features, Scenario Outline , Where you can pass ( weekdays, post code, number of days) as variables


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

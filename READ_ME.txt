QA Engineer Test 
 
This is a very simple website that checks to see if a vehicle exists.  
 
The object is to write the acceptance criteria that you think is appropriate in the gherkin syntax. 
 
You are free to implement the automated acceptance criteria using any language and framework of your choice, however, try and keep the usage of the third-party library to a minimum.  
 
Data 
 
Registration Number: OV12UYY URL: https://covercheck.vwfsinsuranceportal.co.uk/ 

RUNNING THE TESTS

All test scenarios are in feature files located in the features folder. I have created 3 different relevant scenario files:
1. home_page.feature
2. vehicle_check_negative.feature
3. vehicle_check_positive.feature

To run these scenario tests you will have to enter the following behave command in the terminal, making sure you are in the virtual environment (venv) via your IDE (PyCharm) and in the location where this read me file is located:
1.	behave vehicleCheck\features\home_page.feature
2. 	behave vehicleCheck\features\vehicle_check_negative.feature
3.	behave vehicleCheck\features\vehicle_check_positive.feature


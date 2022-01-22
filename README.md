#Collecting data on farmer seed choice in India
##About the project
Seed choice for farmers is a complex decision. This involves understanding what kind of seeds are available to farmers (for instance, genetically modified seeds), what technology is best suited to them based on their geography and cultivation practices, and what are the regulatory challenges they might face. 

To collection information on these parameters, I have created the backend of a survey to be hosted on the WhatsApp API. India has 390.1 million monthly active users on WhatsApp. While WhatsApp penetration is greater in urban India, WhatsApp users in rural areas are increasing at a rapid pace. In this context, a WhatsApp survey to understand challenges faced by farmers will ensure a large-scale response. I initially built this in response to a J-PAL call for developers on a similar project.  

##How to run the code
The code has five parts to it. These are constants.py, utils.py, exception_handler.py, logger_util.py, and driver.py. 

- **constants.py:** This sets the constraints for User IDs and invalid submissions (length of ID, authorised User IDs, and successful submissions). 
- **utils.py:** This sets the responses for login and information endpoints.
- **exception_handler.py:** This sets the response for an error-ridden entry or an exception. 
- **logger_util.py:** This stores the log records of the application in "log_file_test.log". 
- **driver.py:** This is the main part of the code and incorporates utils.py and exception_handler.py. In order to get the application online, you need to run driver.py. Once it is active, you should get the notification of "Debugger is active!". 


##Once the application is up and running
This program runs in three sections:
1. **Starting page:**  To start the program once you run the code, open http://localhost:5050/ on your browser. It should throw up the following instruction:

    *"Please enter one of the end points: /login, /seed_choices, /challenges or /cultivation_practices."* 
2. **Login:** When you attempt to log in, you can use three user IDs, 123456, 334455, 908768, to gain authorised access. While running the program for a survey, this becomes a crucial checkpoint where only farmers or users that are meant to be surveyed participate in the event. In practice, these user IDs can be government-issued. Use http://localhost:5050/login?user_id=123456 to access the login endpoint and replace the user ID as per your choice. 

    If you use an authorised user ID (for example, 123456), you would get the following result: 
    *User 123456 authorised to log in to the portal!.*

    If you use an unauthorised user ID (for example, 123457), you would get the following result:  
    *"Unauthorised login by User 123457."*
3. **Information submission**: Once you have logged in, you can access any of the information-related endpoints by entering the sample browser calls. For example, use http://localhost:5050/seed_choices?user_id=123456&gmo_crops to enter information about choosing genetically modified crops. For successful submission, you should use one of 'true', 'yes', '1' (for example, http://localhost:5050/seed_choices?user_id=123456&gmo_crops=true). It will give you the following notification:

    *"User 123456 successfully submitted seed choices."*

##Next steps
This is only a sample of what the backend could look like. I would like to host it on the WhatsApp API and play with the user interface.

####*About me*
I am a policy researcher based in New Delhi, India. You may reach out to me at sudhakar.tarini@gmail.com.  

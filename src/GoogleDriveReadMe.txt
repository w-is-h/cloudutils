Tu use this install:
	google-api-python-client
		easy_install --upgrade google-api-python-client
		 - or -
		pip install --upgrade google-api-python-client
	
	python filesystem
		pip install fs
		 - or -
		download and install from: https://code.google.com/p/pyfilesystem/


1. Go to https://console.developers.google.com/flows/enableapi?apiid=drive and register your application, if you have not already done this. 
2. Don't forget to enable the Drive API for your application in the google developers console.
3. Go to Credentials in the google developers console under "Client ID for web applications" set your redirect URI - this is the URI to which you will be redirected once once you allow your application to use google drive. 
4. Copy all the necesarry information from the "Client ID for web applications" to cloudutils_config.py.

After all of this is done you can start using this module. Please note that google drives doesn't work with paths but with IDs so for everything you will need to write the ID of a file not its name. A small example(enter this code line by line):

from cloudutils_factory import CloudutilsFactory

fact = CloudutilsFactory()
#This will raise an exception if you are doing it for the first time.
# The exception is the URL you should use to allow this app to access your 
# google drive. 
fact.getGoogleDriveFS()

fs = fact.getGoogleDriveFS("enter here the code you have received as a result in the previous step")
#Code example: 4/I45KA5dDy0cneFTHo1bsTGQkWwCX.0kxY32AGgxAYYFXr95uygvWpXo2UjgJ

fs.makedir("/first_new_folder")
#Now you can go to google drive and check if everything is OK

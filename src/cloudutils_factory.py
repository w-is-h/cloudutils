from oauth2client.client import OAuth2WebServerFlow
from datetime import datetime
from cloudutils_config import *
from GoogleDriveFS import GoogleDriveFS
from cloudutils import CloudRedirectUrl

class CloudutilsFactory:
    def getGoogleDriveFS(self, code=None):
        try:
            credentials = self.readFromFile()
            return GoogleDriveFS(CFG_GOOGLE_DRIVE_ROOT, credentials) 
        except:
            pass
        
        if code is None:
            flow = OAuth2WebServerFlow(CFG_GOOGLE_DRIVE_CLIENT_ID, 
                CFG_GOOGLE_DRIVE_CLIENT_SECRET,
                CFG_GOOGLE_DRIVE_SCOPE,
                CFG_GOOGLE_DRIVE_REDIRECT_URI,
                approval_prompt='force')
            url = flow.step1_get_authorize_url()
            raise CloudRedirectUrl(url)

        flow = OAuth2WebServerFlow(CFG_GOOGLE_DRIVE_CLIENT_ID,
                CFG_GOOGLE_DRIVE_CLIENT_SECRET,
                CFG_GOOGLE_DRIVE_SCOPE,
                CFG_GOOGLE_DRIVE_REDIRECT_URI,
                approval_prompt='force')
        credentials_new = flow.step2_exchange( code )
        
        credentials = {
            'access_token': credentials_new.access_token,
            'client_id': credentials_new.client_id,
            'client_secret': credentials_new.client_secret,
            'refresh_token': credentials_new.refresh_token,
            'token_expiry': datetime.strftime(credentials_new.token_expiry, "%Y, %m, %d, %H, %M, %S, %f" ),
            'token_uri': credentials_new.token_uri,
            'user_agent': credentials_new.user_agent,
            'root': CFG_GOOGLE_DRIVE_ROOT
        }
        self.saveToFile(credentials)
        return GoogleDriveFS(CFG_GOOGLE_DRIVE_ROOT, credentials)
    
    def saveToFile(self, credentials):
        f = open("credentials_gd.txt", "w")

        f.write(credentials['access_token'] + "\r\n")
        f.write(credentials['client_id'] + "\r\n")
        f.write(credentials['client_secret'] + "\r\n")
        f.write(credentials['refresh_token'] + "\r\n")
        f.write(credentials['token_expiry'] + "\r\n")
        f.write(credentials['token_uri'] + "\r\n")
        try:
            f.write(credentials['user_agent'] + "\r\n")
        except:
            f.write("None" + "\r\n")

        f.write(credentials['root'] + "\r\n")

        f.close()
    
    def readFromFile(self):
        try:
            f = open("credentials_gd.txt", "r")
        except:
            return None

        credentials = {
            'access_token': f.readline().strip(),
            'client_id': f.readline().strip(),
            'client_secret': f.readline().strip(),
            'refresh_token': f.readline().strip(),
            'token_expiry': f.readline().strip(),
            'token_uri': f.readline().strip(),
            'user_agent': f.readline().strip(),
            'root': f.readline().strip()
        }
        f.close()
        return credentials



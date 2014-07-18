""" Configuration for all cloud services and general cloudutils config."""

# General configuration
CFG_CLOUD_UTILS_ROWS_PER_PAGE = 10

CFG_SERVICE_PRETTY_NAME = { 'dropbox': "Dropbox", 
                            'google_drive': "Google Drive",
                            'skydrive': "SkyDrive"
                           }

CFG_CLOUD_UTILS_ENABLED_SERVICES = ['dropbox', 'google_drive', 'skydrive']

# Dropbox configuration
CFG_DROPBOX_KEY = "123"
CFG_DROPBOX_SECRET = "123"
CFG_DROPBOX_ACCESS_TYPE = "app_folder"
CFG_DROPBOX_ROOT = "/"
CFG_DROPBOX_CSRF_TOKEN = "dropbox_auth_csrf_token"



# Google drive configuration
CFG_GOOGLE_DRIVE_CLIENT_ID = "123"
CFG_GOOGLE_DRIVE_CLIENT_SECRET = "123" 
CFG_GOOGLE_DRIVE_SCOPE = "https://www.googleapis.com/auth/drive"
CFG_GOOGLE_DRIVE_ROOT = "/" 
CFG_GOOGLE_DRIVE_REDIRECT_URI = "http://localhost"

# SkyDrive configuration
CFG_SKYDRIVE_CLIENT_ID = "123"
CFG_SKYDRIVE_CLIENT_SECRET = "123"
CFG_SKYDRIVE_SCOPE = ["wl.skydrive_update", "wl.offline_access"]
CFG_SKYDRIVE_ROOT = "/"

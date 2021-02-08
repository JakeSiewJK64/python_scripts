from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from  google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import google.oauth2.credentials
import os
import pickle

SCOPES = "https://www.googleapis.com/auth/spreadsheets"
CREDENTIALS = "credentials.json"
API_VERSION = "v4"
API_SERVICE_NAME = "sheets"
SPREADSHEET_ID = "1R8EBLAWJy3qkIKtq43hB6sNI7-JWQKDtrAWhM1y2UIY"
RANGE_NAME = "Class Data!A2:E"

# def get_authenticated_service():
    # flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, SCOPES)
    # credentials = flow.run_console()
    # return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
    
# if __name__ == '__main__':
    # # when running locally, disable OAuthlib's HTTPs verification.
    # # running in production do not leave this option enabled
    # os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    # service = get_authenticated_service()

def get_authenticated_service():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    # checks if the credentials are invalid of do not exists
    if not credentials or not credentials.valid:
        # checks if the credentals have expired
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Requests())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, SCOPES)
            credentials = flow.run_console()
        # save the credentials
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
    
# calling the API
service = build("sheets", "v4", CREDENTIALS)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values',[])
for row in values:
    print('%s, %s' % (row[0], row[4]))
    
if __name__ == '__main__':
    main()


































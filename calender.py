from oauth2client.service_account import ServiceAccountCredentials

from Google import Create_Service

scopes = 'https://www.googleapis.com/auth/calendar'
creds = ServiceAccountCredentials.from_json_keyfile_name('BirthdayReminder.json', scopes)



service = Create_Service(creds, 'calender', 'v3', scopes)
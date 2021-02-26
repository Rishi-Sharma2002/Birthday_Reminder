import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('BirthdayReminder.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Birthdays').sheet1


# print(type(sheet.get_all_records()))

for i in sheet.get_all_records():
    if(i.Name == "Rishi"):
        print(i)
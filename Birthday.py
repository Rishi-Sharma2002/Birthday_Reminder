import schedule
import datetime
import gspread
import pandas as pd
import re
import subprocess
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('BirthdayReminder.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Birthdays').sheet1

# class Birthdays:
#     def find_birthdays(self):
#             for i in sheet.get_all_records():
#                 if(i["Date"] == "17/8"):
#                     print("Happy Birthday ", i["Name"])
   


# if __name__ == '__main__':
#     b = Birthdays()
    
#     # schedule.every().day.at('11:06').do(b.find_birthdays)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(5)
current_date = datetime.datetime.now()
# current_date = current_date.read().decode("utf-8")
current_date = re.search(rb'-\d\d-\d\d', current_date)
print(current_date)

import schedule
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import date
import Google

scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/calendar']
creds = ServiceAccountCredentials.from_json_keyfile_name('BirthdayReminder.json', scopes)
client = gspread.authorize(creds)

sheet = client.open('Birthdays').sheet1
# service = Create_Service(creds, 'calender', 'v3', scopes[2])
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

print(date.current_date())
for i in sheet.get_all_records():
    if(i["Date"] == date.current_date()):
        Google.send(i["Name"])

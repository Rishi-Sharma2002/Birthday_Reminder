import datetime
import re



def regex(current):
        current = str(current)
        date = re.search(r'-\d\d-\d\d', current)
        return date.group(0)

def current_date():
        date = datetime.datetime.now()
        date = regex(date)
        return date

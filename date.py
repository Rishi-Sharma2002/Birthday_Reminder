import datetime
import re
class date:
    def current_date():
        date = datetime.datetime.now()
        return date
    
    def regex(current):
        current = str(current)
        date = re.search(r'-\d\d-\d\d', current)
        return date.group(0)



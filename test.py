import json

from datetime import datetime
from dateutil import tz
from pytz import timezone
 
format = "%Y-%m-%d %H:%M:%S %Z%z"

# Opens text file
with open('test.txt', 'r') as p:
    my_items = p.read()

# Tunrs string intp json
response = json.loads(my_items)
# Prints json real pretty
json_formatted = json.dumps(response, indent=4)

# Prints json
print(json.dumps(response['timelines']['hourly'][0], indent=4))

# Grabs all of the times
time = [i['time']  for i in response['timelines']['hourly']] 


from_zone = tz.tzutc()
to_zone = tz.tzlocal()

#x = datetime.time.fromutc(time[0])

print(x)
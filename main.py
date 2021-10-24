from ShinePattern import ShinePattern
from TimeKeeper import TimeKeeper
from HttpFriend import HttpFriend
from AccessPointFriend import AccessPointFriend

from machine import RTC
import time
#ap = AccessPointFriend("HackMePlz", 2)
#ap.start()

shine = ShinePattern()
tk = TimeKeeper()
tk.add_alarm("1", [2021, 10, 23, 17, 42, 0, 0, 0], shine.set_pattern, "SOLID_RED", True, False)
alarms = tk.list()
print(alarms[0].name())
print(alarms[0].is_daily())
print(alarms[0].is_weekdays_only())
print(alarms[0].alarm_time())
print(alarms[0].is_enabled())
alarms[0].disable()
print(alarms[0].is_enabled())
alarms[0].enable()
tk.poll()
print(alarms[0].alarm_time())

#rtc = RTC()
#rtc.datetime([2021, 10, 17, 17, 23, 0])
#print time.time()

#http = HTTPFriend()
#http.start_server()
#http.serve()



#from ShinePattern import ShinePattern
#from TimeKeeper import TimeKeeper
from HttpFriend import HttpFriend
from RouteBuddy import RouteBuddy
from TextCrawler import TextCrawler
#from AccessPointFriend import AccessPointFriend

import time

def now():
    t = time.localtime(time.time())
    return f"{t[3]:02}:{t[4]:02}:{t[5]:02} {t[0]:04}-{t[1]:02}-{t[2]:02}"

tc = TextCrawler("index.html")
def index_route(tc):
    tc.define("now", now())
    return tc.make()

rb = RouteBuddy()
rb.new_route("/", index_route, tc, mimetype="text/html")
rb.new_route(
    "/get_local_datetime.js",
    rb.static_document,
    "get_local_datetime.js",
    "text/javascript")


#from machine import RTC
#import time
#ap = AccessPointFriend("HackMePlz", 2)
#ap.start()

#shine = ShinePattern()
#tk = TimeKeeper()
#tk.add_alarm("1", [2021, 10, 23, 17, 42, 0, 0, 0], shine.set_pattern, "SOLID_RED", True, False)
#alarms = tk.list()
#print(alarms[0].name())
#print(alarms[0].is_daily())
#print(alarms[0].is_weekdays_only())
#print(alarms[0].alarm_time())
#print(alarms[0].is_enabled())
#alarms[0].disable()
#print(alarms[0].is_enabled())
#alarms[0].enable()
#tk.poll()
#print(alarms[0].alarm_time())

#rtc = RTC()
#rtc.datetime([2021, 10, 17, 17, 23, 0])
#print time.time()

http = HttpFriend()
http.start_server()
http.serve(rb)



from ShinePattern import ShinePattern
from TimeKeeper import TimeKeeper
from HttpFriend import HttpFriend
from RouteBuddy import RouteBuddy
from AccessPointFriend import AccessPointFriend

import json

shine = ShinePattern()
tk = TimeKeeper()

def now(req):
    return tk.now()

def index_route(req):
    return static_document("index.html", req);

def set_time(req):
    print(req["payload"])
    time_to = json.loads(req["payload"])
    tk.set(time_to)
    return "{}"

def next_pattern(res):
    shine.next_pattern()
    return "{}"

def get_alarms(res):
    return json.dumps(tk.list())

def add_alarm(res):
    alarm = json.loads(req["payload"])
     
rb = RouteBuddy()
rb.new_route("/", index_route, None, mimetype="text/html")
rb.new_route(
    "/get_local_datetime.js",
    rb.static_document,
    "get_local_datetime.js",
    "text/javascript")
rb.new_route("/device_time", now, None, mimetype="text/html")
rb.new_route("/set_time", set_time, None, mimetype="application/json") 
rb.new_route("/next_pattern", next_pattern, None, mimetype="application/json")
rb.new_route("/get_alarms", get_alarms, None, mimetype="application/json")
rb.new_route("/add_alarm", add_alarm, None, mimetype="application/json")

#from machine import RTC
#import time
ap = AccessPointFriend("HackMeForReal", 2)
ap.start()

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



#from ShinePattern import ShinePattern
#from TimeKeeper import TimeKeeper
from HttpFriend import HttpFriend
from RouteBuddy import RouteBuddy
from TextCrawler import TextCrawler
#from AccessPointFriend import AccessPointFriend

def hello(arg):
    print(arg)
    return arg

tc = TextCrawler("index.html")
tc.define("now", "this present moment")

rb = RouteBuddy()
rb.new_route("Hello", hello, "Bonjour Monde", None)
rb.new_route("/", [hello, tc.make], None, "text/html")
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



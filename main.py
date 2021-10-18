from ShinePattern import ShinePattern
from HttpFriend import HttpFriend
from AccessPointFriend import AccessPointFriend

from machine import RTC
import time
#ap = AccessPointFriend("HackMePlz", 2)
#ap.start()

shine = ShinePattern()

TIMESTAMP_OFFSET = 946713600 #Correct for y2k epoch

rtc = RTC()
rtc.datetime([2021, 10, 17, 17, 23, 0])
print time.time()

#http = HTTPFriend()
#http.start_server()
#http.serve()



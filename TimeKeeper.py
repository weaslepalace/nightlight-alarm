from machine import RTC
import utime


    
class TimeKeeper:
    
    class AlarmHandler:
        
        def __init__(self, callback, arguments):
            self._callback = callback
            self._arguments = arguments
        
        def call(self):
            self._callback(self._arguments)

        def arguments(self):
            return self._arguments 

    class AlarmEvent:

        _DAYS_OF_THE_WEEK = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Satruday",
            "Sunday"
        ]
        
        def _is_today_a_weekend(self, now):
            today = self._DAYS_OF_THE_WEEK[utime.localtime(now)[6]]
            its_a_weekend = today is "Saturday" or today is "Sunday"
            return its_a_weekend
            
        def _next_alarm_time(self, t):
            date = list(utime.localtime(t))
            date[2] += 1
            return utime.mktime(date)

        def __init__(self, name, alarm_time, handler, daily, weekdays_only):
            self._alarm_time = utime.mktime(alarm_time)
            self._handler = handler
            self._daily = daily
            self._weekdays_only = weekdays_only
            self._enabled = True
            self._name = name
        
        def dispatch(self):
            self._handler.call()
        
        def check(self):
            now = utime.time()
            
            enabled = {
                self._enabled is True and
                self._is_today_a_weekend(now) is True and
                self._weekdays_only is True
            }        
            expired = utime.time() >= self._alarm_time

            if expired is True:
                self.dispatch() if enabled is True else None
                self._alarm_time = self._next_alarm_time(self._alarm_time)

            done = expired is True and enabled is True and self._daily is True
            return done

        def enable(self):
            self._enabled = True
        
        def disable(self):
            self._enabled = False

        def is_enabled(self):
            return self._enabled

        def is_daily(self):
            return self._daily
        
        def is_weekdays_only(self):
            return self._weekdays_only
    
        def name(self):
            return self._name

        def alarm_time(self):
            return utime.localtime(self._alarm_time)

    _alarms = []
    
    def __init__(self):
        pass

    def add_alarm(self,
        name, alarm_time,
        callback, arguments,
        daily, weekdays_only):

        alarm_id = len(self._alarms)
        handler = self.AlarmHandler(callback, arguments)
        event = self.AlarmEvent(name, alarm_time, handler, daily, weekdays_only)
        self._alarms.append(event)
        return alarm_id

    def remove_alarm(self, alarm=None, alarm_id=None, name=None):
        if alarm is not None:
            self._alarms.remove(alarm)
        elif alarm_id is not None:
            del self._alarms[alarm_id]
        elif name is not None:
          self._alarms.remove([a for a in self._alarms if a.name is name][0])

    def poll(self):
        for alarm in self._alarms:
            done = alarm.check()
            if done is True:
                remove_alarm(alarm)

    def list(self):
        return self._alarms

    def set(self, time):
        
    def now(self):
        
        

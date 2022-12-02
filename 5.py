from time import time, localtime

class Clock:

    @staticmethod

    def say_time():
        say_time = localtime(time())
        return print(f'{say_time.tm_hour}:{say_time.tm_min}:{say_time.tm_sec}')

Clock.say_time()
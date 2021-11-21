import time
am = 'A.M.'
pm = 'P.M.'

class Clock():
    def __init__(self, hour, minute, second, clock_type=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    def tick(self):
        self.second = self.second + 1
        if self.second >= 60:
            self.minute = self.minute + 1 
            self.second = 0 
        if self.minute >= 60:
            self.hour = self.hour + 1
            self.minute = 0
    
    def __str__ (self):
        zone = am 
        if self.hour >= 12:
            zone = pm
        if self.clock_type == 0:
            pass
        else:
            time = self.hour
            if time == 0:
                time = 12
            if time >= 12:
                time = time - 12
                return (f'{self.hour}:{self.minute}:{self.second} {zone}')
            if time <= 12:
                return (f'{self.hour}:{self.minute}:{self.second} {zone}') 

def main():
    hour = int(input('Input hours '))
    minute = int(input('Input minute '))
    second = int(input('Input second '))
    clock = Clock(hour, minute, second,1)
    while True:
        print(clock)
        clock.tick()
        time.sleep(1)

main()


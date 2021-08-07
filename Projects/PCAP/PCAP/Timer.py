class Timer:
    def __init__(self, hh=0, mm=0, ss=0):
        self.__val = hh, mm, ss

    def __str__(self):
        return "{:02}:{:02}:{:02}".format(*self.__val) 

    def shift(self, delta):
        # Calculate time as the number of seconds from the start of counting shifted by `delta`:
        next_second = 3_600*self.__val[0] + 60*self.__val[1] + self.__val[2] + delta
        
        ss = next_second % 60
        mm = (next_second - ss) % 3_600 // 60
        hh = next_second // 3_600 % 24
        self.__val = hh, mm, ss

    def next_second(self):
        self.shift(1)
        

    def prev_second(self):
        self.shift(-1)

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
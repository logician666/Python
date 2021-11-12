class TimeInterval:
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def __add__(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes
        hours   = self.hours   + other.hours

        minutes, seconds = minutes + seconds // 60, seconds % 60
        hours, minutes = hours + minutes // 60, minutes %60

        return TimeInterval(hours, minutes, seconds)

t1, t2 = TimeInterval(1, 20, 3), TimeInterval(2, 30, 5)

print(t1, t2, sep='\n')
print(t1 + t2)


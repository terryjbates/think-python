"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        minutes = hour * 60 + minute
        self.int_time = (minutes * 60) + second
        
    def __str__(self):
        minutes, second = divmod(self.int_time, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self):
        print str(self.int_time)

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.int_time

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.int_time > other.int_time

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.int_time + other.int_time
        return seconds

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        return Time(seconds + self.int_time)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.int_time < 0:
            return False
        return True


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    start = Time(9, 45, 00)
    print "Start time"
    start.print_time()

    print "Time after increment of 1337 seconds"
    end = start.increment(1337)
    end.print_time()

    print 'Is end after start?',
    print end.is_after(start)

    print 'Using __str__'
    print start, end

    start = Time(9, 45)
    duration = Time(1, 35)
    print start + duration
    print start + 1337
    print 1337 + start

    print 'Example of polymorphism'
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print total


if __name__ == '__main__':
    main()

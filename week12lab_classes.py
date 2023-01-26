
import time

class Clock:
    #constructor taking values for hours, minutes, seconds and clock_type
    def __init__(self, hours, minutes, seconds, clock_type=0):
        #assigning values, assuming everything is valid
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock_type = clock_type
    
  
    def tick(self):
        
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        # wrapping around and updating hours if minutes>60
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1
        # wrapping around hours if hours>24
        if self.hours > 2:
            self.hours = 0
    
    
    def __str__(self):
        #checking if it is 24 hr clock
        if self.clock_type == 0:
            #simply returning time in hh:mm:ss format
            return '{:02d}:{:02d}:{:02d}'.format(self.hours, self.minutes, self.seconds)
        else:
            #assuming current time is AM
            s = "AM"
            #if hours>=12, setting s to PM
            if self.hours >= 12:
                s = "PM"
            #assigning hours to a variable
            h = self.hours
            #if hours is 0, setting h to 12 (0 hours in 24 clock is 12 am in 12 hr clock)
            if self.hours == 0:
                h = 12
            #otherwise if hours>12, subtracting 12 from hours to get it under 12
            elif self.hours > 12:
                h = self.hours - 12
            #returning a properly formatted string with all details
            return '{:02d}:{:02d}:{:02d} {:s}'.format(h, self.minutes, self.seconds, s)


#reading hours, minutes and seconds 
h=int(input("What is the current hour ==> "))
m=int(input("What is the current minute ==> "))
s=int(input("What is the current second ==> "))

#creating a Clock (12 hour)
c=Clock(h,m,s,1)
#looping infinitely (user will have to terminate the program manually)
while True:
    #printing time
    print(c)
    #ticking by 1 second
    c.tick()
    #pausing for 1 second
    time.sleep(1)





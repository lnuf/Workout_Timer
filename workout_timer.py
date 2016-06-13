# workout_timer.py
#Timer with 5 counting modes

import time

mode_choice=int(input("Please Enter a Mode (1=Timer, 2=Stopwatch, 3=EMOM, 4=TABATA, or 5=Custom Interval)"))

def formatTime(x):
    minutes = int(x / 60)
    seconds_rem = int(x % 60)
    if (seconds_rem < 10):
        return(str(minutes) + ":0" + str(seconds_rem))
    else:
        return(str(minutes) + ":" + str(seconds_rem))

#Mode 1: count down timer
def count_down():
    x = int(input("Enter number of seconds: "))
    for i in range(x + 1):
        time.sleep(1)
        if x==0:
            print "STOP"
        else:
            print(formatTime(x))
        x -= 1

#Mode 2: Stopwatch

#Mode 3: EMOM
def every_minute():
    no_min=int(input("Enter number of minutes: "))
    x=no_min*60
    for i in range(x+1):
        time.sleep(1)
        min_check=int(x%60)
        if min_check==0 & x!=0:#BUG-Doesn't print GO
            print "GO"
            x-=1
        elif x==0:
            print "STOP"
        else:
            print(formatTime(x))
            x-=1
#Mode 4: TABATA
def tabata():
    rounds=int(input("Enter Number of Rounds"))
    while rounds>0:
        x=0
        for i in range(x,31):
            time.sleep(1)

            #print(i)
            if i==30:
                print "REST"

            elif x==0:
                print "GO"
            else:
                print(formatTime(x))
            x+=1
        rounds-=1



#Call Mode function
if mode_choice==1:
    print "Timer"
    count_down()
elif mode_choice==2:
    print "Stopwatch"
elif mode_choice==3:
    print "EMOM"
    every_minute()
elif mode_choice==4:
    print "TABATA"
    tabata()
elif mode_choice==5:
    print "Custom Interval"
else:
    print "Mode not found"

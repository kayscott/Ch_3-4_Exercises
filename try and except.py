age = raw_input('how old were you when you got a car?') 
try : 
    x = int(age)
    if x > 16:
        print'cool story bro' 
    else: 
        if x < 16:
            print'you are totally not old enough to drive' 
except : 
    print'please enter a number' 
     
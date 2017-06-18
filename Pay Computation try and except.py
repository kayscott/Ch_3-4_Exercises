hours = raw_input('How many hours did you work?') 
r1 = raw_input('Enter Rate') 
try: 
    h1 = int(hours)
    r1 = float(r1)
    if h1 <= 40 : 
        print h1 * r1 
    else :
        if h1 > 40 : 
            print (40 * r1) + ((h1 - 40) * (r1 * 1.5))
except : 
    print 'please enter numeric input' 
    
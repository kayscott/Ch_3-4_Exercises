#conditional basic 
x = raw_input('How old are you?') 
if x > 18 :
    print 'Congratulations you are an adult!' 
    
#conditional mutli-way 
kids = raw_input('How many kids do you have?')
y = int(kids)
if y >= 1 : 
    print 'you are a parent' 
    if y > 5 : 
        print 'but your creating a village'
else : 
    print 'not parents' 
    
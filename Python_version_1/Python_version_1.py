import datetime

x = datetime.date.today() ##Have to change formating

##Can make the rest of the code in for loops
#Displays the required dates
m = datetime.timedelta(1) #Contains all the fromating to treat datetime etc. like integers
x = x+m
print(x)
m = datetime.timedelta(3)
x = x+m
print(x)
m = datetime.timedelta(7)
x = x+m
print(x)
m = datetime.timedelta(21)
x = x+m
print(x)
m = datetime.timedelta(30)
x = x+m
print(x)
m = datetime.timedelta(45)
x = x+m
print(x)
m = datetime.timedelta(60)
import datetime

days = [1, 3, 7, 21, 30, 45, 60]


x = datetime.date.today() ##Have to change formating

##Can make the rest of the code in for loops
#Displays the required dates
for i in days:
    m = datetime.timedelta(i) #Contains all the fromating to treat datetime etc. like integers
    x = x-m
    print(x)
    print("")
    input("Press enter when done to proceed to the next")
    print("")

input('Press ENTER to exit')


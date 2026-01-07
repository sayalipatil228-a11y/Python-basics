import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# https://docs.python.org/3/library/time.html#time.strftime

if(timestamp <"12"):
    print("Good morning!")
elif(timestamp <"17"):
        print("Good afternoon!")
elif(timestamp <"21"):
        print("Good evening!")
else:
        print("Good night!")

# Good morning!
time = int(input("Enter time in hours (0–23): "))

if time >= 5 and time < 12:
    print("Good Morning")
elif time >= 12 and time < 17:
    print("Good Afternoon")
elif time >= 17 and time < 21:
    print("Good Evening")
else:
    print("Good Night")

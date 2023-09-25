import time

input_time = int(input("enter the time(seconds) : "))

for i in range(input_time,0, -1):
    seconds = int(i%60)
    minutes = int((i/60)%60)
    hours = int((i/3600))
    print(f"{hours:02}: {minutes:02} : {seconds:02} \r")
    time.sleep(1)
print("TIME'S UP")
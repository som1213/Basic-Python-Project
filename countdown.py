import time  
my_time = int(input("Enter your time :"))
for x in range(my_time,0,-1):
    secands = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{secands:02}")
    time.sleep(1)
print("Time's up")
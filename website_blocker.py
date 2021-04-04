import platform
import time
from datetime import datetime as dt

plt = platform.system()

if plt == "Windows":
   host_path = "C:\Windows\System32\drivers\etc\hosts"
else:
    host_path = "\etc\hosts"

redirect_url = "127.0.0.1"

website_list = ["www.facebook.com","facebook.com","www.prothomalo.com","prothomalo.com"]

print(website_list)

#print(dt(dt.now().year,dt.now().month,dt.now().day,10))

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("working hours...")
    else:
        print("fun hours...")
    time.sleep(5)
from time import sleep 
from datetime import datetime
while True :
    t = datetime.now() .strftime('%H:%M:%S')
    print(t, end='\r' )
    sleep(1)
import time

wt=1
max_retries=5
tr=0

while tr<max_retries:
    print("attempts",tr+1,"wt",wt)
    time.sleep(wt)
    wt*=2
    tr+=1
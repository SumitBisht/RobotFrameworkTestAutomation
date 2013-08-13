import time

var = []
while(time.time()%10 <8):
	var.append(int(time.time()%10))
	time.sleep(1)

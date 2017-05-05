from tqdm import *
from time import *
import threading
import requests 

f = open('../docs/dic','r')
f_list = f.readlines()
num = len(f_list)

global lists
lists =[]
time1 = time()

def find_url(url,list):
	#read file try to request url in dic 
	global lists
	# pbar = tqdm(list)
	for f_list in list: 
		urls = url+'/'+f_list[:-1]
		s = requests.get(url=urls).status_code
		if s != 404:
			lists.append(urls+' '+str(s))		
		# pbar.set_description("Processing %s" % f_list)
	
# to create & start threadings
def thread(url,size):
	a = [1]*size
	for i in range(size):
		a[i] = threading.Thread(target=find_url,args=(url,f_list[i*num/size:(i+1)*num/size]))

	for t in a:
		t.setDaemon(True)
		t.start()
	# to wait anyone of the threadings 
	i = 1
	while i:
		i = 0
		for t in a:
			if t.isAlive() == True:
				i = 1

	print time()-time1 
	# for i in lists:
	# 	print i


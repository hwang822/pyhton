import thread
import time
 
# Define a function for the thread
def process(person, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        #material = count
        print("%s material %s at time %s" % (person, count, time.ctime(time.time())))
 
# Create two threads as follows
try:
    thread.start_new_thread( process, ("Producer produces", 1, ) )
    thread.start_new_thread( process, ("Consumer consumes", 2, ) )
except:
    print("Error: unable to start thread")
 
while 1:
    pass
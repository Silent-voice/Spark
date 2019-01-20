import time
import datetime
print time.time()
s = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
print s
print type(s)
import logging
from rediscluster import RedisCluster
from datetime import datetime
import pytz
import time

startup_nodes = [{"host":"jjjtest-cm.7825uk.clustercfg.apn2.cache.amazonaws.com", "port":"6379"}]
n = input("How many keys? : ")
#n = 1000

### Write Operation ###

def time():
    time.time = datetime.now().astimezone(pytz.utc)

def write():
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)
    start = datetime.now().astimezone(pytz.utc)
    for write_num in range(int(n)):
        rc.set('TestKey_' + str(write_num), 'Value_' + str(n))
    end = datetime.now().astimezone(pytz.utc)
    print("From " + str(start) + " to " + str(end) + " / writing for " + str(end - start) + "sec.")
    print(str(n) + " Keys were written.")


### Read Operation ###

def read():
    logging.basicConfig()
    logger = logging.getLogger('rediscluster')
    logger.setLevel(logging.DEBUG)
    logger.propagate = True
    # option for comparing to readonly mode
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)
#    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True, readonly_mode=True)
#    rc = RedisCluster(startup_nodes,startup_nodes, decode_responses=True, skip_full_coverage_check=True, read_from_replicas=True)
    start = datetime.now().astimezone(pytz.utc)
    for read_num in range(int(n)):
        rc.get('TestKey_' + str(read_num))
    end = datetime.now().astimezone(pytz.utc)
    print('''
###############################
           Summary
###############################''')
    print("From " + str(start) + " to " + str(end) + " / reading for " + str(end - start) + "sec.")
    print(str(n) + " Keys were read.")

menu = '''
### Operations ###
 1. Write
 2. Read
 3. Both

Which operation do you want to execute? : '''

if __name__ == '__main__':
    ans = input(menu)
    if ans == '1':
        write()
    elif ans == '2':
        read()
    elif ans == '3':
        write()
        read()
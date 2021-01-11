import os
import time
from subprocess import call


cnt = 0
for i in range(1, len(os.listdir('test')) // 2 + 1, 1):
    cmd = "cp test/" + str(i) + ".in stacking.in"
    os.system(cmd)
    start_time = time.time()
    call(["python", "2012_Jan_stacking.py"])
    print("--- %s seconds ---" % (time.time() - start_time))
    cmd = "diff test/" + str(i) + ".out stacking.out"
    result = os.system(cmd)
    if (result == 0):
        print("testcase " + str(i) + " works")
        cnt += 1
    else:
        print("testcase " + str(i) + " failed")
print(str(cnt) + "/10")
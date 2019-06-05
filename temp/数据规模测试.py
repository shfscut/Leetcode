# @Time: 2019-05-25 13:49
# @Author: 'haifeng.shi@klook.com'
import time
changes = []

t, num = 0, 0
for i in range(1000000):
    t_new = time.process_time()
    if t_new != t:
        num += 1
    t = t_new
changes.append(('process_time()', num))

t, num = 0, 0
for i in range(1000000):
    t_new = time.perf_counter()
    if t_new != t:
        num += 1
    t = t_new
changes.append(('perf_counter()', num))

print(changes)
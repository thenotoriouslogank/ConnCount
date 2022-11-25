import os
with open(r"ip.tmp", 'r') as fp:
    for count, line in enumerate(fp):
        pass
total = count + 1
os.remove("ip.tmp")
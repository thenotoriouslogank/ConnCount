import os

def GetTotal():
    with open(r'ip', 'r') as fp:
        for count, line in enumerate(fp):
            pass
    total = count + 1
    os.remove('ip')
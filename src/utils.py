import random
import time

def randomShuffle(data):
    shuffled = data[:]
    random.shuffle(shuffled)
    return shuffled

def timeStamp(prefix="ID"):
    epochTime = int(time.time())
    return f"{prefix}{epochTime}"
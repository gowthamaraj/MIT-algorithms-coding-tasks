import random

def list_gen(n):
    randomlist = []
    for i in range(0,n):
        n = random.randint(1,100)
        randomlist.append(n)
    return(randomlist)
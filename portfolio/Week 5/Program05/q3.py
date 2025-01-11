import sys
from sys import argv

list=argv[1:]
list.sort(key=len)
print(list)
try:
    print(f"the shortest word is: {list[0]}")
except:
    print("Word is not passed")
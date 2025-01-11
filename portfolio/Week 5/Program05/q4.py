import sys
from sys import argv
from urllib.request import urlopen
from urllib.error import *

try:
    user_link=argv[1]
    link=urlopen(user_link)

except IndexError as i:
    print("No url provided and", i)

except HTTPError as h:
    print("HTTP Error",h)

except URLError as h:
    print("URL Error",h)

else:
    print("Page found successfully!")
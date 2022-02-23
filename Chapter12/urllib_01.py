# This script does exactly the same than socket_01.py
import urllib.request

# make request and treat the response as a file.
# No need for GET request, nor a while True loop or anything like it.
# This takes care of everything, and I can read it line-by-line as if it was file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# I won't get headers printed!

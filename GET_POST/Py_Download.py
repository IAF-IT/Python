from urllib import request
import sys

myUrl = "http://adv400.tripod.com/kartinka.jpg"
myFile = "C:\\Users\\iafar\\Desktop\\kartinka.jpg"

try:
    print("Start downloading file")
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("Warning")
    print(sys.exc_info()[1])
    exit()

print("File downloaded and saved")
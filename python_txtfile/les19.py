import sys

filename = "user.txt"    # user != users

while True:
 try:
     print("Inside TRY")
     myfile = open(filename, mode='r', encoding="Latin-1")
 except Exception:
     print("Inside EXCEPT")
     print("Error found!")
     print(sys.exc_info()[1])
     filename = input("Enter Correct file name ! : ")

#    sys.exit()
 else:
     print("Inside ELSE")
     print(myfile.read())
     sys.exit()
#  finally:
#     print("Inside FINALLY")

print("=====================EPF=====================")



#myfile = open(filename, mode='r', encoding='Latin-1')

#print(myfile.read())
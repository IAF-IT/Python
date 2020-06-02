import sys
import os

# print("Hello")

# print(sys.argv[1:])
# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("Help requested")
        print("Usage of this program is : python3 pycli.py arg1 arg2 ....")
    print("Arguments enter: " + str(sys.argv[1:]))
else:
    print("Argument NOT PROVIDED")

print("\n")

os.system("pwd")
inputfile = "rockyou.txt"
outputfile = "users.txt"

passw = "nano"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')

for num, line in enumerate(myfile1):
    if passw in line:
        print(str(num) + " : " + line.strip())
        myfile2.write(line)


 #    user = open(inputfile, mode='w', encoding='latin_1')

myfile1.close()
myfile2.close()
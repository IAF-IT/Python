import re

input_file = "dump.html"
result_file = "result.txt"

inputfile = open(input_file, mode='r', encoding='Latin-1')
resultfile = open(result_file, mode='w', encoding='Latin-1')
mytext = inputfile.read()

lookfor = r"[\w\.]+\@[\w]+\.(?!org)[\w]+"        # - исключаю 'org' ---- (?!org)


results = re.findall(lookfor, mytext)


for item in results:
    print(item)
    resultfile.write(item + "\n")



print("total :" +str(len(results)))
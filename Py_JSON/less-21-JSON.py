import json

filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')


player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["ORIGON", "NY", "NV"]

}

player2 = {
    'PlayerName': "Hillary Clinton",
    'Score': 346,
    'awards': ["WI", "TX", "MI"]

}


myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# -------------- Save JSON --------------
json.dump(myplayers, myfile)

myfile.close()

# --------- Load by JSON ------------

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print("------------------------\n")
    print("name is : " + str(user['PlayerName']))
    print("score : " + str(user['Score']))
    print("awards : " + str(user['awards'][0]))
    print("awards : " + str(user['awards'][1]))
    print("awards : " + str(user['awards'][2]))
    print("------------------------\n")


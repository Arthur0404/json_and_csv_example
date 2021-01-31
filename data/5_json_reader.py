import  json

with open("..//files/user.json") as data_json:
    users = json.loads(data_json.read())
    list_json = users
    for user in list_json:
        print(user['company'])

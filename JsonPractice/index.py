import json

data = '''{
    "name" : "Chuck",
    "phone" : {
          "type" : "intl:",
          "number" : "+ 1734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('User count:',len(info))

for item in info:
    print('Name:', info["name"])
    print('Hide:', info["email"]["hide"])
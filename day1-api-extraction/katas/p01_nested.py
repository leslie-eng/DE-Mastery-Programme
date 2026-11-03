USERS = [
    {"id": 1, "name": "Leanne Graham", "email": "Sincere@april.biz", 
"address": {"city": "Gwenborough"}},
    {"id": 2, "name": "Ervin Howell", "email": "Shanna@melissa.tv", 
"address": {"city": "Wisokyburgh"}},
    {"id": 3, "name": "Clementine Bauch", "email": "Nathan@yesenia.net", 
"address": {"city": "McKenziehaven"}},
    {"id": 4, "name": "Jack Bauer", "email":"jack@gmail.com",}
]

# print one line per user 
for user in USERS:
    print(f"the name: {user.get('name')} and the city: {user['address']['city']}")
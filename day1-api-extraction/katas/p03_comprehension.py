USERS = [
    {"id": 1, "name": "Leanne Graham", "email": "Sincere@april.biz", 
"address": {"city": "Gwenborough"}},
    {"id": 2, "name": "Ervin Howell", "email": "Shanna@melissa.tv", 
"address": {"city": "Wisokyburgh"}},
    {"id": 3, "name": "Clementine Bauch", "email": "Nathan@yesenia.net", 
"address": {"city": "McKenziehaven"}},

]

emails = [(user.get('email', {})).lower() for user in USERS]

for user in USERS:
    email = user.get('email', "")

id_name = { user.get("id", None) : user.get("name", None)
            for user in USERS
    
        }

city_w_m = [user.get("address", {}).get("city", "unknown")
    for user in USERS
    if str(user.get("address", {}).get("city", "unknown")).startswith(("W", "M"))
 
]

city_m_w = list(filter(lambda user: str(user.get("address", {}).get("city", "")).startswith(("W", "M"))  , USERS))

print(emails)
print(id_name)
print(city_w_m)


USERS = [
    {"id": 1, "name": "Leanne Graham", "email": "Sincere@april.biz", 
"address": {"city": "Gwenborough"}},
    {"id": 2, "name": "Ervin Howell", "email": "Shanna@melissa.tv", 
"address": {"city": "Wisokyburgh"}},
    {"id": 3, "name": "Clementine Bauch", "email": "Nathan@yesenia.net", 
"address": {"city": "McKenziehaven"}}
    
]

nan = float("nan")

def extract_core_fields(user):
    return {
        "customer_id": user.get("id", None),
        "name": user.get("name", None),
        "email": user.get("email", None),
        "city": (user.get("address") or {}).get("city", nan),
    }
    

def build_structures(users):
    core_dicts = [extract_core_fields(i)
        for i in users
    ]
    records = {user["customer_id"] : extract_core_fields(user)
        for user in core_dicts
    }
    
    return core_dicts, records

#print(extract_core_fields(USERS[0]))
#extract_core_fields({"id": 4, "name": "X", "email": "x@y.z"}))
# extract_core_fields({"id": 4, "name": "X", "email": "x@y.z", "address": None})
# print(build_structures(users=USERS))

core_list, by_id = build_structures(USERS)
#print(len(core_list), list(by_id.keys()))
#print(by_id[2]["name"])
print(build_structures([{"id": 1, "name": "A"}, {"id": 1, "name": "B"}]))
#print(by_id[1])

response = {"id" : 1, "name" : "Leslie", "address": {"City": "Nairobi", "geo": {"lat": -34.098}}}

def flatten(record, parent_key="", sep="_"):
    '''flatten the json values of an arbitrary json with infinite loops
    '''
    # start with an empty dictionary  
    flatten_dict = {}
    for key, value in record.items():
        new_key = f'{parent_key}{sep}{key}' if parent_key else key
        if isinstance(value, dict):
            flatten_dict.update(flatten(value, new_key, sep))
        else:
             flatten_dict[new_key.lower()] = value
   
       
            
    return flatten_dict    





# loop through the records and extract the json
# flatten_dict = {}
# for k,v in response.items():
    
#     if isinstance(v, (int, str, float)):
#         flatten_dict[k.lower()] = v 
        
#     elif isinstance(v, dict):
#         for m, n in v.items():
#             if isinstance(n, (int, str, float)):
#                 flatten_dict[f'{k}_{m}'.lower()] = n
    
#             if isinstance(n, dict):
#                 for x, y in n.items():
#                     if isinstance(y, (int, str, float)):
#                         flatten_dict[f'{k}_{m}_{x}'.lower()] = y


                        

print(flatten(response))
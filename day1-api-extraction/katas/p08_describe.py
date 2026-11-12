## type(), recursion for the first time, indentation built into the string
# the print bug from Day 1

def describe_structure(record, level=0):
    '''
    prints one line per key as key: typename, indenting two spaces per level
    and goes into nested dictionaries
    '''
    padding = "  " * level
    #print(padding, type("record").__name__)
    
    for k, v in record.items():
        print(padding,k, f" :{type(v).__name__}" )
        if isinstance(v, list):
            level+=1
            describe_structure(v, level=level)
        
        if isinstance(v, dict):
            level+=1
            describe_structure(v, level=level)
            



response = {"id" : 1, "name" : "Leslie", "address": {"city": "Nairobi", "geo": {"lat": -34.098}}}
# padding = " "

# print(response)
# for k,v in response.items():
#     print(k, f": {type(v).__name__}")
#     if isinstance(v, dict):
#         for i,j in v.items():
#             print(" ", i, f": {type(j).__name__}")
#             if isinstance(j, dict):
#                 for m,n in j.items():
#                     print("  ", m, f": {type(n).__name__}")
# print("=-" * 20)
# print(" " * 10, "hello")

describe_structure(response)
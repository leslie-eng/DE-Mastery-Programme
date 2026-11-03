
def get_nested(data : dict, path : str, default=None):
    "loop through each path and if the data isn't present return default"
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    
    if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
    
    path_list = path.split(".")
    
    current = data
    
    for key in path_list:
        
        if not isinstance(current, dict):
            return default
        
        if key not in current:
            return default
        
        current = current[key]
        
    return current
       
            
            
print(get_nested({"a": 7}, "a.b"))

print(get_nested({"a": {"b": {"c": 5}}}, "a.b.c"))
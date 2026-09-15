# class Name:
#     def __init__(self, name):
#         self.name = name 

# print(Name("vishal").__dict__)
# print(Name("Rahul").__dict__)

# * Generate dict using zip()
# idx = [1,2,3,4,5,6]
# name = ['Vishal', 'Ashish', 'Rahul', 'Dev', 'Rohan', 'Ravi']
# print(dict(zip(idx,name)))
# print(zip(idx, name))
# d = {}.fromkeys(idx,10)
# print(d)

# square = {i:i**2 for i in range(1,10)}
# print(square)

# idx = [1,2,3,4,5,6]
# name = ['Vishal', 'Ashish', 'Rahul', 'Dev', 'Rohan', 'Ravi']
# d = dict(zip(idx,name)) 

# print(d.get(7, "Ram"))
# print(d.values())
# print(d.setdefault(7, 'shyam'))



# ** Learning UPDATE METHOD IN DICTIONARY
config = {
     "color": "green",
     "width": 42,
     "height": 100,
     "font": "Courier",
 }

user_config = {
     "path": "/home",
     "color": "red",
     "font": "Arial",
     "position": (200, 100),
 }
 
# config.update(user_config)
# config.update([("width", 200), ("api_key", 1234)])
# config.update(color="yellow", script="__main__.py")
# print(config)

# ** POP method in DICTIONARY 

# print(config.pop('color'))
# print(config.pop('color', None))
# del config['color']
# print(config)

# ** POPITEMS method in DICTIONARY 

# print(config.popitem())

# d = {}
# d.clear()
# print(d)

# new_config = config.copy()

# print(new_config)
# config[1] = 2
# print(new_config)
# print(config)

#** UNION Operation on DICTIONARY 
 
# new_c = config | user_config 
# print(new_c)

# config |= user_config
# print(config)
# Data Structures - why? How?
# List

environments = ["dev","prd","stg","test"]
#print(environments)
#print(environments[0])
#print(environments[1])

print(len(environments))
# 4
# 0,1,2,3

environments.append("bastion")
print(environments)

#print(dir(environments))

print(environments.insert.__doc__)



# dictionary

device_info = {
    "name" : "Apple Mackbook Pro",
    "Ram" : "16 GB",
    "CPU" : 8,
    "isNew" : False
}

print(device_info.get("isNew"))

device_info.update({"environments":environments})

print(device_info)

# sets

#device_ids = {} # empty dictionary
#device_ids = {1} # set
#print(type(device_ids))

device_ids = {1,2,3,4,4,4,5,6,7,8,9,9,10} # set
#print(len(device_ids))
#new_device_ids = {11,12,13}
#print(device_ids.union(new_device_ids))

new_device_ids = {1,2,11,12,13}
print(device_ids.intersection(new_device_ids))

# tuples

days_of_week = ("Sunday","Monday")



# String Formatting
name = input("Enter your name")

city = input("Enter your city name:")

about = f"Hello Dosto, this is {name} and I am from {city}"

other_name = input("enter the other person name:")

print(about.replace("Dosto",other_name)) #replace is a python function

# It will print what all things i can do with this about
#print(dir(about))

a = 5
print(dir(a))
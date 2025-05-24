"""
a = 10
b = 30
c = 50



if a > b and a > c: # if this line is true then only the control flow goes inside
    print("A is biggest amongst A,B,C")
#    print("Yes, i want to tell again A is bigger")
elif b > a and b > c:
    print("B is bigger")
elif c > a and c > b:
    print("C is the biggest")
else: # if the above condition fails, then it goes to else
    print("all are equal")


    
env = "prd"

if env == "dev":
    print("load dev applicetion")
else:
    print("Not in dev environment")

"""


def check_biggest(a,b,c):
    if a > b and a > c: # if this line is true then only the control flow goes inside
        print("A is biggest amongst A,B,C")
#       print("Yes, i want to tell again A is bigger")
    elif b > a and b > c:
        print("B is bigger")
    elif c > a and c > b:
        print("C is the biggest")
    else: # if the above condition fails, then it goes to else
        print("all are equal")

a = 10
b = 20
c = 30
check_biggest(a,b,c)


# take backups

# code to create backup
# 0000
# 000

#def backup(dir_a,dir_b):
    # code to backup
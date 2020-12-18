
def square(num):
    return num*num

l1=[3,4,2,7]
# method 1
l2=[]
for i in l1:
    l2.append(square(i))
print(l2)

# ----Method 2__
# map(function,list in which u have to apply this function)
print(list(map(square,l1)))

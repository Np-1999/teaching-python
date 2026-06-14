l1 =[1,2,3,4]
l1[0]= 10

l2 = []

for num in l1:
    l2.append(num * 2)

print(l2)


# Key syntax
# for varname (it will store value from list) in listname:
#    body of loop


l3 = []
for i in range(len(l1)-1, -1, -1):
    l3.append(l1[i])

# string
#str_1 = "Nikhil"
#str_1[0] = "A"
#print(str_1)

# tuple
abc = (1,2,3)

# error abc[0] = 4
print(abc[0])

number_to_english = ("zero","one","two")

# dict
dict_1 = {"a":1, "b":2} # uses hashmap 


print(dict_1["a"])

for key, value in dict_1.items():
    print(f"Key ={key} value = {value}")


# reverse indexing
l1 = [1,2,6,4] 
print(l1[-1])
# list comprehension
l2 = [num for num in l1 if num % 2 == 0]


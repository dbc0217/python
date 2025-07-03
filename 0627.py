list_a=[1,3,5,"234","56"]
# print(list_a[0]+list_a[4])
# print(list_a[-2]+list_a[-1])
# print(list_a[-1:-3])
# print(list_a[-3:-1])
# print(list_a[:])
# print(list_a[0:9])
# print(list_a[4:1:-1])
# print(list_a[1::-1])

# import copy
# list_b = copy.deepcopy(list_a)
# list_a.append("a")
# print(list_a)
# # list_a.append([4,5,6])
# # print(list_a,list_a[6],list_a[6][2])
# print(list_b)

# list_d = [1,2,3,[7,8,9]]
# # list_e = list_d[:]
# list_d.append(6)
# # print(list_d,list_e)
# import copy
# list_f = copy.deepcopy(list_d)
# list_d[3].append(10)
# print(list_d,list_f)
# list_d[2]=5
# print(list_d,list_f)
# list_d.insert(3,3)
# print(list_d,list_f)

# list_1 = ["a",'bc',"a"]
# list_2 = ["def",'ghij']
# list_2.extend(list_1)
# # print(list_2)
# del list_2[0]
# # print(list_2)
# list_2.remove("a")
# list_2.remove("a")
# print(list_2)

# pop_thing = list_2.pop(-2)
# print(list_2,pop_thing)

# fruits = ["apple","banana","coconut","dragon fruit"]
# index = int(input("輸入0~3:"))
# fruit = fruits[index]
# print(fruit=="banana")
# if fruit =="apple":
#     print("蘋果" )
# elif fruit =="banana":
#     print("香蕉" )
# else:
#     print("其他" )
price = [30,50,80,110]
index = 2
p = price[index]
if p<=25:
    print("A")
elif p<=60:
    print("B")
else:
    print("C")

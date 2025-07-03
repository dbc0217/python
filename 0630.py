# account_data = ["z0630","s0630","t0630","e0630"]
# account = input("請輸入帳號:")
# print(account in account_data)

# if account in account_data:
#     print("有此帳號")
# else:
#     print("無此帳號")

# for i in range(0,12,5): #第二個逗點後是步數
#     print(i)

# for i in [1,3,5,7,9]:
#      print(i)

# number_list = []
# even_list = []
# for i in range(1,101):
#     number_list.append(i)
#     if i%2==0:
#         even_list.append(i)
#     # print(number_list)

# print(number_list)
# print(even_list)
# total = 0
# for num in number_list:
#     print(total,num)
#     total += num  # total = total + num
#     print(total)

# total = 0
# for num in number_list:
#     print(f"目前 total: {total}, num: {num}")
#     total += num  # total = total + num
#     print(f"目前總和: {total}")

# for i in range(1,8):
#     if i == 3:
#         continue
#     elif i == 5:
#         break
#     print(i)

# count = 0
# while count<6:
#     if count==0:
#         print("從零開始")
#     else:
#         print(f"數到 {count}")
#     count += 1

# 波浪動畫
# import time

# style = "*************"
# width = 20
# step = 0
# direction = 1

# while True:
#     print(" "*(step)+style)
#     step += direction
#     if(step >= width) or (step <= 0):
#         direction *= -1
#     time.sleep(0.2)

# zip() 並排合併
# a = [1,2,3,4]
# b = ["apple","banana","cat","dog"]
# zip_ab = zip(a,b)
# print(zip_ab)  # <zip object at 0x000002C29BF7EF80>

# list_ab = list(zip_ab)
# print(list_ab)
# for num,word in list_ab:
#     print(f"編號: {num}, 單字: {word}")

person_1 = {
    "name":"小明",
    "年齡": 25,
    "居住地":"台北"
    }

update_data = {
    "job":"工程師",
    "居住地":"台南"
    }

person_1.update(update_data)
print(person_1)

print(
f"""name: {person_1["name"]}
年齡: {person_1["年齡"]}
居住地: {person_1["居住地"]}""")
person_1["性別"] = "男"
person_1["居住地"] = "台中"
print(person_1)

# get()
age_1 = person_1.get("年齡","這筆資料沒有年齡的key")
height_1 = person_1.get("height","這筆資料沒有height的key")
print(age_1)
print(height_1)

print(list(person_1.keys()))
print(list(person_1.values()))
person_1_items = list(person_1.items())
print(person_1_items)
print(len(person_1))  

for i in person_1:
    print(i)
    print(person_1[i])

for key,value in person_1_items:
    print(key,value)










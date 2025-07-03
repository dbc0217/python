# num_list = [2,5,7,8]
# target = 9
# index_list = []
# for i in range(0,len(num_list)):
#     for j in range(i+1,len(num_list)):
#         if num_list[i] + num_list[j] == target:
#             index_list.append(i)
#             index_list.append(j)
# print(index_list)

# num_list = [2,5,7,8]
# target = 9
# index_list = []

# num_dict = {}
# for i in range(0,len(num_list)):
#     diff = target - num_list[i]
#     if num_list[i] in num_dict:
#         index_list.append(num_dict[num_list[i]])
#         index_list.append(i)
#     num_dict[diff] = i  # {7:0,4:1, ...}
# print(index_list)

# even_set = {2,4,6,8}
# odd_set = {1,3,5,7}

# word = "letters"
# # print(set(word))
# word_list = ["a","a","a","b","b","c","d","aaa"]
# # print(set(word_list))
# person_1 = {"name":"小明","年齡": 25,"居住地":"台北"}
# print(set(person_1))  # key

# Alice_hobbies = {"閱讀","游泳","旅行","電影"}
# Bob_hobbies = {"電影","旅行","籃球","音樂"}
# common_hobbies = Alice_hobbies & Bob_hobbies  #交集
# print(common_hobbies)
# all_hobbies = Alice_hobbies | Bob_hobbies  # 聯集
# print(all_hobbies)
# #差集
# only_Alice_hobbies = Alice_hobbies - Bob_hobbies
# print(only_Alice_hobbies)
# only_Bob_hobbies = Bob_hobbies - Alice_hobbies
# print(only_Bob_hobbies)

# mixed_data = {
#     "name": "小明",
#     "age": 25,
#     "height": 172.5,
#     "hobbies": ["閱讀","打球"],
#     "scores": {"math":90,"Eng": 85},
#     "birthday" :(1999,7,1)
# }
# # 1.print(mixed_data["name"],mixed_data["height"])
# # 2.b_hobbies_list = mixed_data["hobbies"]
# print(b_hobbies_list[1])
# # 2-1mixed_data["hobbies"][0] = "唱歌"
# mixed_data["hobbies"].append("R.A.P")
# print(mixed_data)
# # 3.print(mixed_data["scores"]["Eng"])
# # 3-1total = mixed_data["scores"]["Eng"] + mixed_data["scores"]["math"]
# mixed_data["scores"]["total"] = total
# print(mixed_data)
# # 4.year,month,day = mixed_data["birthday"]
# print(year,month,day)

def f(x):
    result = 2*x + 3
    return result

for num in range(1,6):
    print(f(num))

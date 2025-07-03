# def animal_sound(animal):
#     if animal == "dog":
#         print("汪汪")
#     elif animal == "cat":
#         print("喵喵")
#     elif animal == "bird":
#         print("啾啾")
#     elif animal == "rabbit":
#         print("蛤")
#     else:
#         print("沒有")

# while True:
#     animal = input("輸入動物(英文),或是輸入X結束迴圈: ")
#     if animal in "Xx":
#         print("退出迴圈")    
#         break
#     animal_sound(animal)

def triangle_type(a,b,c):
    a,b,c = sorted([a,b,c])

    if a+b<=c:
        return "不是一個三角形"
    elif a**2 + b**2 == c**2:
        return "直角三角形"
    elif a**2 + b**2 < c**2:
        return "鈍角三角形"
    elif a**2 + b**2 > c**2:
        return "銳角三角形"
    
# while True:
#     a = int(input("輸入第一邊長:"))
#     b = int(input("輸入第二邊長:"))
#     c = int(input("輸入第三邊長:"))
#     print(triangle_type(a,b,c))

# import random
# def guess_the_number(start = 1, end = 100):
#     print(f"終極密碼開始,範圍是{start}~{end}")
#     target = random.randint(start,end)
#     while True:
#         guess_num = int(input('輸入你要猜的整數:'))
#         if guess_num == target:
#             print("恭喜")
#             break
#         elif guess_num > target:
#             print(f"範圍是{start} ~ {guess_num}")
#             end = guess_num
#         elif guess_num < target:
#             print(f"範圍是{guess_num} ~ {end}")
#             start = guess_num
    
# # guess_the_number()
# guess_the_number(start = 100, end = 200)

# def add_to_order(item,result = None):
#     if result == None:
#         result = []
#     result.append(item)
#     return result
# menu = None
# while True:
#     meal = input("要點什麼: ")
#     menu = add_to_order(meal,menu)  #item,result
#     print(menu)

# def say_hello(name):
#     return "Hello " + name
# print(say_hello("a"))

# def square(x):
#     result = x**2
#     return result

# print(square(9))

# def is_even(number):
#     if number%2 == 0:
#         return True
#     else:
#         return False
# print(is_even(2))

# def print_args(arg1,*args):
#     print(arg1)
#     print(args)

# print_args(1,1,4,4,8,4,4,4,"a","2","bbb","c","d")

# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(name="小明",age=18,city="台北")

def num_generate(times):
    for i in range(times):
        print(f"內部{i}")
        yield i
for i in num_generate(10):
    print(f"外部{i}")


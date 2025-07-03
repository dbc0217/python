class Person():
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def introduce (self):
        return f"Hi! My name is {self.name}.I'm {self.age} years old."
    def is_adult (self):
        return self.age >= 18
    def set_age (self, new_age):
        if new_age <0:
            print("年齡不能為負數")
        else:
            self.age = new_age  
# 呼叫物件
# person_1 = Person("Alice",18)
# print(person_1.name)  # self.name 的 name
# print(person_1.age)  # self.age 的 age
# print(person_1.introduce())
# print(person_1.is_adult())
# person_1.set_age(54)  #沒有return
# print(person_1.age)

# person_2 = Person("Bob",15)
# print(person_2.name)  # self.name 的 name
# print(person_2.age)  # self.age 的 age
# print(person_2.introduce())
# print(person_2.is_adult())

class Student(Person):
    def __init__ (self, name, age, student_id , grade):
        super().__init__(name,age)
        self.student_id = student_id
        self.grade = grade
        self.scores = {}
    def study(self):
        return f"I'm {self.name}. I'm studying in grade {self.grade}. My ID is {self.student_id} ."
    def scores_data(self, subject, score):
        self.scores[subject] = score
        return self.scores

# student_1 = Student("Amy",9,"S30323",3)
# print(student_1.age)
# print(student_1.name)
# print(student_1.student_id)
# print(student_1.grade)
# print(student_1.introduce())
# print(student_1.is_adult())
# print(student_1.study())
# print(student_1.scores_data("math",90))
# print(student_1.scores_data("eng",95))
# print(student_1.scores_data("math",85))
# print(student_1.scores)

class Pet():
    def __init__(self , name , animal_type , age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.p = {}
    def pet_info (self):
        self.p["Name"] = self.name
        self.p["animal_type"] = self.animal_type
        self.p["age"] = self.age
        return self.p
    
# pet_1 = Pet("aespa","貓",3)
# print(pet_1.pet_info())



        
from class0703 import Person,Student,Pet
def main():
    person = Person("Alice",18)
    student = Student("Amy",9,"S30323",3)
    pet = Pet("aespa","貓",3)

    print(f"Hi! I'm{person.name}. I have a student,{student.name}. She has a pet,named{pet.name}")
    print(student.introduce())
if __name__ == "__main__":
    main()
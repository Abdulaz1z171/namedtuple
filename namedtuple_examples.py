from collections import namedtuple

# Student = namedtuple('Student',['full_name','age','course','field'])
# john = Student('John Smith', '24','1-course','Energetic')
# modified = john._replace(full_name = 'Alex Brown')



"""
Car = namedtuple('Car',['model','color','year','price'])
car1 = Car('Gentra','white','2021','$20000')
print(car1.price)
print(car1.color)
print(car1._replace(color = 'blue'))
(Car._make(['Cobalt','green','2015','$12000']))
"""



"""
Phone = namedtuple('Phone',['model','color','CPU','price'],)
phone1 = Phone('Xiomi r7','black','7 CPU','$120')
print(phone1._asdict())
"""



"""
University = namedtuple('University',['name','location','number_of_fields','number_of_students'])
university1 = University('TATU','Tashkent','35 fields','18000')
# print(university1)
university1 = university1._replace(number_of_students = '25000')
print(university1)
"""


Person = namedtuple('Person','name age gender',defaults = ['18','male'])
person1 = Person('Alex')
print(person1._fields)
print(Person._field_defaults)


students = []
def add_information_by_namedtuple_fuction():
    while input('Do you want to add information to our university? ') != 'no':
        name = input('What is your name? ')
        age = input('How old are you? ')
        course = input('What is your course?')
        field = input('What is your field? ')
        Student  = namedtuple('Student',['name','age','course','field'])
        student1 = Student(name,age,course,field)
        if student1 not in students:
            students.append(student1)
        else:
            continue
    else:
        print(students)


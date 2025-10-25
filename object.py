class Person:
    def __init__(self,in_name,in_last_name,in_age):
        self.name=in_name
        self.last_name=in_last_name
        self.age=in_age

    def Person_print(self):
        print(f'name is {self.name}  last name is {self.last_name}  age is {self.age} ')

class Person2(Person):
    def __init__(self,in_number,in_National_ID_number,in_id):
        self.number=in_number
        self.National_ID_number=in_National_ID_number
        self.id=in_id

    def __str__ (self):
        return f' number  is {self.number} in_National_ID_number is {self.National_ID_number} in_id is {self.id} '
#--------------------------------------------------------------------------
x=Person('John','Smith',19)
x.Person_print()

x.name=' Mikey'

y=Person2(1212,863862,77)
print(y)


print(f' name  is {x.name}  lst name is {x.last_name} ')
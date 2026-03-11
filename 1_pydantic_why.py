
def insert_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('Age cant be negative')
        else:
            print(name)
            print(age)
            print("inserted into database")
    else:
        raise TypeError('Incorrect Dataype')
    

def update_patient_data(name:  str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Updated')
    else:
        raise TypeError('Incorrect datatype')
    
insert_patient_data('Arpit',21)



# Dynamic typing means:

# You don’t have to declare the data type of a variable.
# Python automatically decides the type at runtime.

# x = 10
# print(type(x))   # int

# x = "Hello"
# print(type(x))   # str

# x = 3.14
# print(type(x))   # float
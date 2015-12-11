class Pet:
    def __init__(self,name,animal_type,age):

        self.__name=name
        self.__animal_type=animal_type
        self.__age=age
    def set_name(self,name):
        self.__name=name
    def set_animal_type(self,animal_type):
        self.__animal_type=animal_type

    def set_age(self,age):
        self.age=age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
def main():
    name= input("enter name")
    animal_type=input("enter")
    age=input("enter age")
    my_pet=Pet(name,animal_type,age)
    print(my_pet.get_name())
    print(my_pet.get_animal_type())
    print(my_pet.get_age())

main()
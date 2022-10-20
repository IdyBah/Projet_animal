class Pet:
    def __init__ (self,name,animalType,age):
        self.__name=name
        self.__animalType=animalType
        self.__age=age
    def get_name(self):
        return self.__name
    def get_animalType(self):
        return self.__animalType
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name=name
    def set_animalType(self,animalType):
        self.__animalType=animalType
    def set_age(self,age):
        self.__age=age
print("------Debut------")
nom=input("Donner le nom de l'animal:")
typeanimal=input("Donner le type de l'animal:")
age=int(input("Donner l'age de l'animal:"))
Para=Pet(nom,typeanimal,age)
print("Le nom de l'animal: est",Para.get_name(),"Son type est:",Para.get_animalType(),"Il est age de :",Para.get_age())
        
        
        

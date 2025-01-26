class person:
    name="anonymous"
    @classmethod
    def changename(cls,name):
        cls.name=name


p1=person()
p1.changename("parag")        
print(p1.name)
print(person.name)
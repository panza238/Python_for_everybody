
class PartyAnimal(object):
    """My first Python Class
    This is a template to create PartyAnimal objects"""
    x = 0

    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)


an = PartyAnimal()  # Instantiate
an.x = 10  # Change the instance variable
an.party()  # invoke method
an.party()
an.party()
PartyAnimal.party(an) # Use the same method, but "form outside" the object

# TYPING
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))

# printing dir info:
print("\n")
print(an.__doc__)
print(an.__dict__)

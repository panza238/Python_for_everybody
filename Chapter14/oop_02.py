class PartyAnimal:
   x = 0

   def __init__(self):
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)


an = PartyAnimal()
an.party()
an.party()
# No need to specify that you want to destruct the object
# Simply reasigning something else to the variable invokes the __del__ method
an = 42
print('an contains',an)


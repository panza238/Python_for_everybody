class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, nam):
     self.name = nam
     self.num = 10
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)


s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()

# Also... class vs instance variable
PartyAnimal.x = 11
m = PartyAnimal("Mary")
print(m.x)

# x is equal for every instance, it CAN be changed.
# self.num is specific to each instance. It CANNOT be changed

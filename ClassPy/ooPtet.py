class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, z):
     self.name = z
     print(self.name,"constructed")

   @property      
   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
r = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()
r.party()

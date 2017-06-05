class PartyAnimals:
    x = 0
 # nam = ""
    def __init__(self,nam):
        self.nam = nam
        print self.nam, "constructed"
    def party(self):
        self.x = self.x + 1
        print self.nam, "So far", self.x
    def __del__(self):
        print self.nam, "destructed"

class FootballFan(PartyAnimals):
    points = 0
    def touchdown(self):
        self.points=self.points+7
        self.party()
        print self.nam, "points", self.points, ", x is", self.x

s = PartyAnimals("Sally")
s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()


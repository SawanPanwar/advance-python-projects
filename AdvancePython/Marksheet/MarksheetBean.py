class MarksheetBean:
    def __init__(self):
        self.id =0
        self.rollNo = 0
        self.name = ''
        self.physics = 0
        self.chemistry = 0
        self.maths = 0

    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def setRollNo(self, rollNo):
        self.rollNo = rollNo
    def getRollNo(self):
        return self.rollNo
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setPhysics(self, physics):
        self.physics = physics
    def getPhysics(self):
        return self.physics
    def setChemistry(self, chemistry):
        self.chemistry = chemistry
    def getChemistry(self):
        return self.chemistry
    def setMaths(self, maths):
        self.maths = maths
    def getMaths(self):
        return self.maths

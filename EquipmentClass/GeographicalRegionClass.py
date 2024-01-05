class GeographicalRegion:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        
class SubGeographicalRegion(GeographicalRegion):
    def __init__(self, ID, name, Region):
        self.name = name
        self.ID = ID
        self.Region = Region
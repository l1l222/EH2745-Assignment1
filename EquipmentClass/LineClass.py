class ACLineSegment:
    def __init__(self, ID, name, description, EquipmentContainer, r, x,
                 bch, length, gch, aggregate, BaseVoltage, r0, x0,
                 b0ch, g0ch, shortCircuitEndTemperature):
        
        self.ID = ID
        self.name = name
        self.description = description
        self.EquipmentContainer = EquipmentContainer
        self.r = r
        self.x = x
        self.bch = bch
        self.length = length
        self.gch = gch
        self.aggregate = aggregate
        self.BaseVoltage = BaseVoltage
        self.r0 = r0
        self.x0 = x0
        self.b0ch = b0ch
        self.g0ch = g0ch
        self.shortCircuitEndTemperature = shortCircuitEndTemperature
        self.type = 'ACLineSegment'
        self.pd_line = ''
        
class Line:
    def __init__(self, ID, name, Region):
        self.ID = ID
        self.name = name
        self.Region = Region
        self.type = 'Line'
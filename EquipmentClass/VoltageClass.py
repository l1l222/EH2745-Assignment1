class BaseVoltage:
    def __init__(self, ID, nominalVoltage):
        self.ID = ID
        self.nominalVoltage = nominalVoltage
        
class VoltageLevel:
    def __init__(self, ID, name, lowVoltageLimit, highVoltageLimit, Substation, BaseVoltage):
        self.ID = ID
        self.name = name
        self.lowVoltageLimit = lowVoltageLimit
        self.highVoltageLimit = highVoltageLimit
        self.Substation = Substation
        self.BaseVoltage = BaseVoltage
        self.nominalVoltage = ''
        
class BusbarSection:
    def __init__(self, ID, name, EquipmentContainer, ipMax, nominalVoltage = 'null'):
        self.ID = ID
        self.name = name
        self.EquipmentContainer = EquipmentContainer
        self.ipMax = ipMax
        self.type = 'BusbarSection'
        self.nominalVoltage = nominalVoltage
        self.pdbus = 'null'
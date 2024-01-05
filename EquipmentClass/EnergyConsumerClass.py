class EnergyConsumer:
    def __init__(self, ID, name, description, aggregate, EquipmentContainer,
                 LoadResponse = None, p = 0, q = 0):
        
        self.type = 'EnergyConsumer'
        self.pd_bus = 'null'
        self.pd_EC = 'null'
        
        if LoadResponse == None:
            self.ID = ID
            self.name = name
            self.description = description
            self.aggregate = aggregate
            self.EquipmentContainer = EquipmentContainer
            self.p = p
            self.q = q
            
        else:
            self.ID = ID
            self.name = name
            self.description = description
            self.aggregate = aggregate
            self.EquipmentContainer = EquipmentContainer
            self.LoadResponse = LoadResponse
            self.p = p
            self.q = q

class EquivalentInjection:
    def __init__(self, ID, name, description, regulationCapability, r, x, r2, x2, r0, x0, BaseVoltage):
        self.type = 'EquivalentInjection'
        self.ID = ID
        self.name = name
        self.description = description
        self.regulationCapability = regulationCapability
        self.r = r
        self.x = x
        self.r2 = r2
        self.x2 = x2
        self.r0 = r0
        self.x0 = x0
        self.BaseVoltage = BaseVoltage

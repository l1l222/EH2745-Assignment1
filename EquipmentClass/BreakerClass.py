from abc import ABC

class IdentifiedObject(ABC):
    def IdentifiedObject(self):
        pass

class PowerSystemResource(IdentifiedObject):
    def PowerSystemResource(self):
        pass
    
class Equipment(PowerSystemResource):
    def Equipment(self):
        pass


'''
Implement abstract class
'''

class ConductingEquipment(Equipment):
    def __init__(self, phases):
        super().__init__()
        self.phases = phases
        
class Switch(ConductingEquipment):
    def __init__(self, phases, normalOpen):
        super().__init__(phases)
        self.normalOpen = normalOpen
        
class ProtectedSwitch(Switch):
    def __init__(self, phases, normalOpen):
        super().__init__(phases, normalOpen)

class Breaker(ProtectedSwitch):
    def __init__(self, ID, name, aggregate, normalOpen, retained, EquipmentContainer
                 , opened = False):
        self.normalOpen = normalOpen
        self.ID = ID
        self.name = name
        self.aggregate = aggregate
        self.retained = retained
        self.EquipmentContainer = EquipmentContainer
        self.opened = opened
        self.type = 'Breaker'
        self.pd_cb = ''
        
        
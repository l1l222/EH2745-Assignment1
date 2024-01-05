from EquipmentClass.BreakerClass import IdentifiedObject

class Terminal(IdentifiedObject):
    def __init__(self, ID, name, sequenceNumber, phases, ConductingEquipment,
                 ConnectivityNode, description = None, isTraversed = 0,
                 connected = True):
        
        # if description == None:
        #     self.ID = ID
        #     self.phases = phases
        #     self.name = name
        #     self.ConductingEquipment = ConductingEquipment
        #     self.sequenceNumber = sequenceNumber
        #     self.ConnectivityNode = ConnectivityNode
        #     self.traversed = traversed
        #     self.connected = connected
            
        # else:
            self.ID = ID
            self.phases = phases
            self.name = name
            self.ConductingEquipment = ConductingEquipment
            self.sequenceNumber = sequenceNumber
            self.ConnectivityNode = ConnectivityNode
            self.description = description
            self.isTraversed = isTraversed
            self.connected = connected
        
class ConnectivityNode(IdentifiedObject):
    def __init__(self, ID, name, ConnectivityNodeContainer, description = None):
        
        self.pd_bus = ''  
        self.nominalVoltage = ''
        
        if description == None:
            self.ID = ID
            self.name = name
            self.ConnectivityNodeContainer = ConnectivityNodeContainer
            
        else:
            self.ID = ID
            self.name = name
            self.ConnectivityNodeContainer = ConnectivityNodeContainer
            self.description = description
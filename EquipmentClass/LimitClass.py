class OperationalLimitSet:
    def __init__(self, ID, name, description, Terminal):
        self.ID = ID
        self.name = name
        self.description = description
        self.Terminal = Terminal
        
class OperationalLimitType:
    def __init__(self, ID, name, direction, acceptableDuration = None):
        
        if acceptableDuration == None:
            self.ID = ID
            self.name = name
            self.direction = direction
            
        else:
            self.ID = ID
            self.name = name
            self.direction = direction
            self.acceptableDuration = acceptableDuration
class CurrentLimit:
    def __init__(self, ID, name, description, value,
                 OperationalLimitSet, OperationalLimitType):
        self.ID = ID
        self.name = name
        self.description = description
        self.value = value
        self.OperationalLimitSet = OperationalLimitSet
        self.OperationalLimitType = OperationalLimitType

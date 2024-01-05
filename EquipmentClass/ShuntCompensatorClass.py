class LinearShuntCompensator:
    def __init__(self, ID, name, description, normalSections, maximumSections,
                 bPerSection, gPerSection, b0PerSection, g0PerSection, nomU,
                 RegulatingControl, aggregate, EquipmentContainer):
        self.ID = ID
        self.name = name
        self.description = description
        self.normalSections = normalSections
        self.maximumSections = maximumSections
        self.bPerSection = bPerSection
        self.gPerSection = gPerSection
        self.b0PerSection = b0PerSection
        self.g0PerSection = g0PerSection
        self.nomU = nomU
        self.RegulatingControl = RegulatingControl
        self.aggregate = aggregate
        self.EquipmentContainer = EquipmentContainer
        self.type = 'LinearShuntCompensator'
        self.pd_shunt = 'null'
        self.pd_bus = 'null'
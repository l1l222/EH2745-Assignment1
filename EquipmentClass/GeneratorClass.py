class GeneratingUnit:
    def __init__(self, ID, name, description, initialP, nominalP, maxOperatingP,
                 minOperatingP, genControlSource, aggregate, EquipmentContainer,
                 normalPF = 0):
        self.ID = ID
        self.name = name
        self.description = description
        self.initialP = initialP
        self.nominalP = nominalP
        self.maxOperatingP = maxOperatingP
        self.minOperatingP = minOperatingP
        self.genControlSource = genControlSource
        self.aggregate = aggregate
        self.EquipmentContainer = EquipmentContainer
        self.normalPF = normalPF
        
class SynchronousMachine:
    def __init__(self, ID, name, description, aggregate, EquipmentContainer,
                 qPercent, maxQ, minQ, ratedS, Gtype, RegulatingControl,
                 GeneratingUnit, InitialReactiveCapabilityCurve, ratedU,
                 ratedPowerFactor, shortCircuitRotorType, r0, r2, x0, x2,
                 earthingStarPointR, earthingStarPointX, r,
                 satDirectSubtransX, satDirectSyncX, satDirectTransX, mu, ikk,
                 voltageRegulationRange, earthing, p = 0, q = 0, referencePriority = 0,
                 controlEnabled = True):
        self.ID = ID
        self.name = name
        self.description = description
        self.aggregate = aggregate
        self.EquipmentContainer = EquipmentContainer
        self.qPercent = qPercent
        self.maxQ = maxQ
        self.minQ = minQ
        self.ratedS = ratedS
        self.Gtype = Gtype
        self.RegulatingControl = RegulatingControl
        self.GeneratingUnit = GeneratingUnit
        self.InitialReactiveCapabilityCurve = InitialReactiveCapabilityCurve
        self.ratedU = ratedU
        self.ratedPowerFactor = ratedPowerFactor
        self.shortCircuitRotorType = shortCircuitRotorType
        self.r0 = r0
        self.r2 = r2
        self.x0 = x0
        self.x2 = x2
        self.earthingStarPointR = earthingStarPointR
        self.earthingStarPointX = earthingStarPointX
        self.r = r
        self.satDirectSubtransX = satDirectSubtransX
        self.satDirectSyncX = satDirectSyncX
        self.satDirectTransX = satDirectTransX
        self.mu = mu
        self.ikk = ikk
        self.voltageRegulationRange = voltageRegulationRange
        self.earthing = earthing
        self.p = p
        self.q = q
        self.referencePriority = referencePriority
        self.controlEnabled = controlEnabled
        self.type = 'SynchronousMachine'
        self.pd_gen = 'null'

class EnergySource:
    def __init__(self, ID, name, aggregate, EquipmentContainer, r, r0, rn, x, x0, xn, 
                 nominalVoltage, voltageMagnitude, voltageAngle, p = 0, q = 0,):
        self.ID = ID
        self.name = name
        self.r = r
        self.r0 = r0
        self.rn = rn
        self.x = x
        self.x0 = x0
        self.xn = xn
        self.nominalVoltage = nominalVoltage
        self.voltageMagnitude = voltageMagnitude
        self.voltageAngle = voltageAngle
        self.aggregate = aggregate
        self.EquipmentContainer = EquipmentContainer
        self.p = p
        self.q = q
        self.type = 'EnergySource'
        self.pd_gen = 'null'
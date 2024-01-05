class PowerTransformer:
    def __init__(self, ID, name, description, aggregate, EquipmentContainer,
                 beforeShCircuitHighestOperatingVoltage,
                 beforeShCircuitHighestOperatingCurrent,
                 beforeShortCircuitAnglePf, highSideMinOperatingU,
                 isPartOfGeneratorUnit, operationalValuesConsidered):
        self.ID = ID
        self.name = name
        self.description = description
        self.aggregate = aggregate
        self.EquipmentContainer = EquipmentContainer
        self.beforeShCircuitHighestOperatingVoltage = beforeShCircuitHighestOperatingVoltage
        self.beforeShCircuitHighestOperatingCurrent = beforeShCircuitHighestOperatingCurrent
        self.beforeShortCircuitAnglePf = beforeShortCircuitAnglePf
        self.highSideMinOperatingU = highSideMinOperatingU
        self.isPartOfGeneratorUnit = isPartOfGeneratorUnit
        self.operationalValuesConsidered = operationalValuesConsidered
        self.type = 'PowerTransformer'
        self.pd_bus = 'null'
        self.pd_trans = 'null'
        
        
class PowerTransformerEnd:
    def __init__(self, ID, name, r, x, b, g, r0, x0, b0, g0,
                 rground, xground, ratedS, ratedU, endNumber, phaseAngleClock,
                 grounded, connectionKind, BaseVoltage, PowerTransformer,
                 Terminal):
        self.ID = ID
        self.name = name
        self.r = r
        self.x = x
        self.b = b
        self.g = g
        self.r0 = r0
        self.x0 = x0
        self.b0 = b0
        self.g0 = g0
        self.rground = rground
        self.xground = xground
        self.ratedS = ratedS
        self.ratedU = ratedU
        self.endNumber = endNumber
        self.phaseAngleClock = phaseAngleClock
        self.grounded = grounded
        self.connectionKind = connectionKind
        self.BaseVoltage = BaseVoltage
        self.PowerTransformer = PowerTransformer
        self.Terminal = Terminal

class RatioTapChanger:
    def __init__(self, ID, name, neutralU, lowStep, highStep, neutralStep,
                 normalStep, stepVoltageIncrement, ltcFlag, TapChangerControl,
                 tculControlMode, TransformerEnd):
        self.ID = ID
        self.name = name
        self.neutralU = neutralU
        self.lowStep = lowStep
        self.highStep = highStep
        self.neutralStep = neutralStep
        self.normalStep = normalStep
        self.stepVoltageIncrement = stepVoltageIncrement
        self.ltcFlag = ltcFlag
        self.TapChangerControl = TapChangerControl
        self.tculControlMode = tculControlMode
        self.TransformerEnd = TransformerEnd
        
class PetersenCoil:
    def __init__(self, ID, name, aggregate, EquipmentContainer, r,
                 xGroundNominal, xGroundMax, xGroundMin, positionCurrent,
                 offsetCurrent, nominalU, mode):
        self.type = 'PetersenCoil'
        self.ID = ID
        self.name = name
        self.aggregate = aggregate
        self.EquipmentContainer = EquipmentContainer
        self.r = r
        self.xGroundNominal = xGroundNominal
        self.xGroundMax = xGroundMax
        self.xGroundMin = xGroundMin
        self.positionCurrent = positionCurrent
        self.offsetCurrent = offsetCurrent
        self.nominalU = nominalU
        self.mode = mode
        
class PhaseTapChangerAsymmetrical:
    def __init__(self, ID, name, neutralU, lowStep, highStep, neutralStep,
                 normalStep, voltageStepIncrement, xMin, xMax,
                 windingConnectionAngle, TransformerEnd, ltcFlag,
                 TapChangerControl):
        self.ID = ID
        self.name = name
        self.neutralU = neutralU
        self.lowStep = lowStep
        self.highStep = highStep
        self.neutralStep = neutralStep
        self.normalStep = normalStep
        self.voltageStepIncrement = voltageStepIncrement
        self.xMin = xMin
        self.xMax = xMax
        self.windingConnectionAngle = windingConnectionAngle
        self.TransformerEnd = TransformerEnd
        self.ltcFlag = ltcFlag
        self.TapChangerControl = TapChangerControl
        
class TapChangerControl:
    def __init__(self, ID, name, mode, Terminal):
        self.name = name
        self.ID = ID
        self.mode = mode
        self.Terminal = Terminal



import pandapower as pp
from pandapower.plotting import simple_plot
from pandapower.plotting.plotly import vlevel_plotly, simple_plotly
from pandapower.networks import mv_oberrhein
import xml.etree.ElementTree as ET
import webbrowser

from EquipmentClass.BreakerClass import Breaker
from EquipmentClass.VoltageClass import BaseVoltage, VoltageLevel, BusbarSection
from EquipmentClass.TransformerClass import PowerTransformer, PetersenCoil
from EquipmentClass.ConnectivityClass import ConnectivityNode, Terminal
from EquipmentClass.LineClass import Line, ACLineSegment
from EquipmentClass.SubstationClass import Substation
from EquipmentClass.EnergyConsumerClass import EnergyConsumer, EquivalentInjection
from EquipmentClass.GeneratorClass import SynchronousMachine, GeneratingUnit, EnergySource
from EquipmentClass.ShuntCompensatorClass import LinearShuntCompensator



def GatheringData(targetType, grid, ns, ObjectList, constructor):
    for element in grid.findall(targetType, ns):
    # Here, temp contains the elements selected from each given object
        elements = []
        elements.append('#'+element.attrib.get(ns['rdf']+'ID'))
        for temp in element:
        
            # Ignore the item with entsoe
            if 'cim' in temp.tag:
               
                # If there are IDs contained, extract the ID as the attribute
                if ns['rdf']+'resource' in temp.attrib:
                   elements.append(temp.attrib.get(ns['rdf']+'resource'))
                else:
                   elements.append(temp.text)

        ObjectList.append(constructor(*elements))
    return ObjectList


selection = input('Please select the assignment file or reduced file. if you choose 1, it will run Assignment file, if you choose 2, it will run test file'+'\n')

if selection == '2':

    tree = ET.parse('Assignment_EQ_reduced.xml')
    state = ET.parse('Assignment_SSH_reduced.xml')

if selection == '1':

    tree = ET.parse('MicroGridTestConfiguration_T1_BE_EQ_V2-2.xml')
    state = ET.parse('MicroGridTestConfiguration_T1_BE_SSH_V2-2.xml')

'''
tree = ET.parse('MicroGridTestConfiguration_T1_BE_EQ_V2-2.xml')
state = ET.parse('MicroGridTestConfiguration_T1_BE_SSH_V2-2.xml')
'''
grid = tree.getroot()


ns = {'cim':'http://iec.ch/TC57/2013/CIM-schema-cim16#',
      'entsoe':'http://entsoe.eu/CIM/SchemaExtension/3/1#',
      'rdf':'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'}
'''
for equipment in grid:
    if (ns['cim'] in equipment.tag):
        print (equipment.tag.replace("{"+ns['cim']+"}",""))
'''
# First, put ACLineSegment into a list. Before doing this, objects ''ACLineSegment'' are created for all ACLineSegments

ACLineSegment_ = []
ACLineSegment_ = GatheringData('cim:ACLineSegment', grid, ns, ACLineSegment_, ACLineSegment)


'''
for ACLine in grid.findall('cim:ACLineSegment', ns):
    
    # Here, temp contains the elements selected from each ACLineSegment
    ACLineSegment_temp = []
    ACLineSegment_temp.append('#'+ACLine.attrib.get(ns['rdf']+'ID'))
    for temp in ACLine:
        
        # Ignore the item with entsoe
           if 'cim' in temp.tag:
               
               # If there are IDs contained, extract the ID as the attribute
               if ns['rdf']+'resource' in temp.attrib:
                   ACLineSegment_temp.append(temp.attrib.get(ns['rdf']+'resource'))
               else:
                   ACLineSegment_temp.append(temp.text)
                   
    #ACLineSegment_ contains the objects of ACLineSegment
    ACLineSegment_.append(ACLineSegment(*ACLineSegment_temp))
'''

# Next, moving to BaseVoltage
# Breaker Class
Breaker_ = []
Breaker_ = GatheringData('cim:Breaker', grid, ns, Breaker_, Breaker)

BaseVoltage_ = []
for BV in grid.findall('cim:BaseVoltage', ns):
    # Here, temp contains the elements selected from each BaseVoltage
    BV_temp = []
    BV_temp.append('#'+BV.attrib.get(ns['rdf']+'ID'))
    
    for temp in BV:
        
        # Ignore the item with entsoe
        if 'cim' in temp.tag:
               
               # only extract the nominalVoltage
               if 'nominalVoltage' in temp.tag:
                   BV_temp.append(temp.text)
    
    #BaseVoltage_ contains the objects of BaseVoltage
    BaseVoltage_.append(BaseVoltage(*BV_temp))


# Voltage Class
# For busbar section, since the attributes are not in the same order in each busbar.
# It must be carefully treated.
    
BusbarSection_ = []
BusbarSection_ = GatheringData('cim:BusbarSection', grid, ns, BusbarSection_, BusbarSection)

VoltageLevel_ = []
VoltageLevel_ = GatheringData('cim:VoltageLevel', grid, ns, VoltageLevel_, VoltageLevel)

# Connectivity Class
ConnectivityNode_ = []
ConnectivityNode_ = GatheringData('cim:ConnectivityNode', grid, ns, ConnectivityNode_, ConnectivityNode)

Terminal_ = []
Terminal_ = GatheringData('cim:Terminal', grid, ns, Terminal_, Terminal)




PetersenCoil_ = []
PetersenCoil_ = GatheringData('cim:PetersenCoil', grid, ns, PetersenCoil_, PetersenCoil)

#EnergyConsumer
EnergyConsumer_ = []
EnergyConsumer_ = GatheringData('cim:EnergyConsumer', grid, ns, EnergyConsumer_, EnergyConsumer)

EquivalentInjection_ = []
EquivalentInjection_ = GatheringData('cim:EquivalentInjection', grid, ns, EquivalentInjection_, EquivalentInjection)

#GeneratorClass
GeneratingUnit_ = []
GeneratingUnit_ = GatheringData('cim:GeneratingUnit', grid, ns, GeneratingUnit_, GeneratingUnit)

SynchronousMachine_ = []
SynchronousMachine_ = GatheringData('cim:SynchronousMachine', grid, ns, SynchronousMachine_,
                                    SynchronousMachine)

EnergySource_ = []
EnergySource_ = GatheringData('cim:EnergySource', grid, ns, EnergySource_, EnergySource)

# Line Class
Line_ = []
Line_ = GatheringData('cim:Line', grid, ns, Line_, Line)

# ShuntCompensatorClass
LinearShuntCompensator_ = []
LinearShuntCompensator_ = GatheringData('cim:LinearShuntCompensator', grid, ns,
                                        LinearShuntCompensator_, LinearShuntCompensator)


# Transformer Class
PowerTransformer_ = []
PowerTransformer_ = GatheringData('cim:PowerTransformer', grid, ns, PowerTransformer_,
                                  PowerTransformer)

# SubstationClass
Substation_ = []
Substation_ = GatheringData('cim:Substation', grid, ns, Substation_, Substation)


# Read SSH file
for ter in state.findall('cim:Terminal', ns):
    for ele in ter:
        for index, Ter in enumerate(Terminal_):
            if Ter.ID == ter.attrib.get(ns['rdf']+'about'):
                Terminal_[index].connected = ele.text
             
for EC in state.findall('cim:EnergyConsumer', ns):
    for index, power in enumerate(EnergyConsumer_):
        if power.ID == EC.attrib.get(ns['rdf']+'about'):
            EnergyConsumer_[index].p = EC[0].text
            EnergyConsumer_[index].q = EC[1].text
        
for GUnit in state.findall('cim:GeneratingUnit', ns):
    for index, pf in enumerate(GeneratingUnit_):
        if pf.ID == GUnit.attrib.get(ns['rdf']+'about'):
            GeneratingUnit_[index].normalPF = GUnit[0].text
            
for SMachine in state.findall('cim:SynchronousMachine', ns):
    for index, item in enumerate(SynchronousMachine_):
        if item.ID == SMachine.attrib.get(ns['rdf']+'about'):
            SynchronousMachine_[index].p = SMachine[0].text
            SynchronousMachine_[index].q = SMachine[1].text     

for ES in state.findall('cim:EnergySource',ns):
    for index, item in enumerate(EnergySource_):
        if item.ID == ES.attrib.get(ns['rdf']+'about'):
            EnergySource_[index].p = ES[0].text
            EnergySource_[index].q = ES[1].text
                
for breaker in state.findall('cim:Breaker', ns):
    for index, BREAKER in enumerate(Breaker_):
        if BREAKER.ID == breaker.attrib.get(ns['rdf']+'about'):
            Breaker_[index].opened = breaker[0].text


# At last, all components are contained in a dictionary
Components_dict = {'BaseVoltage' : BaseVoltage_,
                   'ConnectivityNode' : ConnectivityNode_,
                   'GeneratingUnit' : GeneratingUnit_,
                   'Substation' : Substation_,
                   'Terminal' : Terminal_,
                   'VoltageLevel' : VoltageLevel_,}

ConductingEquipment_dict = {'PowerTransformer' : PowerTransformer_,
                            'SynchronousMachine' : SynchronousMachine_,
                            'Breaker' : Breaker_,
                            'BusbarSection' : BusbarSection_,
                            'LinearShuntCompensator' : LinearShuntCompensator_,
                            'ACLineSegment' : ACLineSegment_,
                            'EnergyConsumer' : EnergyConsumer_,
                            'EnergySource' : EnergySource_,
                            'EquivalentInjection': EquivalentInjection_,
                            'PetersenCoil' : PetersenCoil_
                            }

# Convert the dictionary of Conducting Equipment into a list
ConductingEquipment_list = []
ConductingEquipment_type_list = []

target = list(ConductingEquipment_dict.values())

for i in range(len(target)):
    for j in range(len(target[i])):
        ConductingEquipment_list.append(target[i][j])

for obj in ConductingEquipment_list:
    ConductingEquipment_type_list.append(obj.type)

class Node_Traversal:
    
    def __init__(self, ID = 'null', CE_type = 'null', node_type = 'null',
                 Terminal_list = [], NoAttached = 0, isTraversed = 0,
                 isAttachedToBusbar = 'null'):

        self.ID = ID # ID of the node
        self.CE_type = CE_type # The type of the CE of the node, not for Terminal
        self.node_type = node_type # Either CE, CN, or Terminal
        self.Terminal_list = Terminal_list # The attached Terminals for CE and CN
        self.NoAttached = NoAttached # Number of attached Terminals for CE and CN
        self.isTraversed = isTraversed # Check if the Terminal node is traversed
        
        # Check if the CN node is connected to busbar
        self.isAttachedToBusbar = isAttachedToBusbar



# Build the nodes of CE(Conducting Equipment)
CE_nodes = []
for CE_object in ConductingEquipment_list:

    CE_terminal_list = []
    
    # Firstly, find the attached terminals.
    for terminal in Terminal_:
        if CE_object.ID == terminal.ConductingEquipment:
            CE_terminal_list.append(terminal)
    #print(CE_object.type,len( CE_terminal_list))

    # Secondly, create a node_traversal for this CE.
    CE_nodes.append(Node_Traversal(CE_object.ID, CE_object.type, 'ConductingEquipment',
                                   CE_terminal_list, len(CE_terminal_list)))

# Build the nodes of CN(Connectivity Node)
CN_nodes = []
for CN_object in ConnectivityNode_:
    
    CN_terminal_list = []
    
    # Firstly, find the attached terminals.
    for terminal in Terminal_:
        if CN_object.ID == terminal.ConnectivityNode:
            CN_terminal_list.append(terminal)
    
    # Secondly, create a node_traversal for this CN
    CN_nodes.append(Node_Traversal(CN_object.ID, 'null', 'ConnectivityNode',
                                   CN_terminal_list, len(CN_terminal_list), 'null', False))
    
# Build the nodes of Terminal
Terminal_nodes = []
for Terminal_object in Terminal_:
    Terminal_nodes.append(Node_Traversal(Terminal_object.ID, 'null', 'Terminal', [],
                                             0, 0, 'null'))
        
        
# Check if the CN is attached to busbar    
for CN_node in CN_nodes:
    for ter in Terminal_:
        if CN_node.ID == ter.ConnectivityNode:
            
            if ter.description == 'Busbar Section':
                CN_node.isAttachedToBusbar = True

def find_next_node(previous_node, current_node):
    
    if previous_node == '':
        previous = ''
    else:
        previous = previous_node.node_type
    
    current = current_node.node_type
    current_ID = current_node.ID
    
    # If the current node is conducting equipment, the next node will be Terminal
    if current == 'ConductingEquipment':
        for CE in ConductingEquipment_dict[current_node.CE_type]:
            if current_ID == CE.ID:

                # Find the next node's type and ID
                for index, ter in enumerate(current_node.Terminal_list):
                    if current_node.NoAttached == 3 and CE.ID == ter.ConductingEquipment:
                        for ter_node in Terminal_nodes:
                            if ter_node.ID == ter.ID:
                                # Return the next node
                                return ter_node

                    elif CE.ID == ter.ConductingEquipment and ter.isTraversed == 0:
                        
                        for ter_node in Terminal_nodes:
                            if ter_node.ID == ter.ID:
                                # Return the next node
                                return ter_node

                    
    # If the current node is ConnectivityNode, the next node will be Terminal
    if current == 'ConnectivityNode':
        for CN in ConnectivityNode_:
            if current_ID == CN.ID:
                
                # Find the next node's type and ID
                for index, ter in enumerate(current_node.Terminal_list):
                    if CN.ID == ter.ConnectivityNode and ter.isTraversed == 0:
                        
                        for ter_node in Terminal_nodes:
                            if ter_node.ID == ter.ID:
                                # Return the next node
                                return ter_node
   
    
    # If the current node is Terminal, then check the previous node's type
    if current == 'Terminal':
        
        # If the previous node is ConnectivityNode, then the next node will be
        # conducting equipment
        if previous == 'ConnectivityNode':
            for ter in Terminal_:
                
                # Using the terminal ID to find the corresponding Terminal object
                if current_ID == ter.ID:
                    for index, CE in enumerate(CE_nodes):
                        if ter.ConductingEquipment == CE.ID:
                            return CE_nodes[index]


                            
        
        # If the previous node is conducting equipment, then the next node will
        # be ConnectivityNode
        elif previous == 'ConductingEquipment' or previous == '':
            for ter in Terminal_:
                
                # Using the terminal ID to find the corresponding Terminal object
                if current_ID == ter.ID:
                    for index, CN in enumerate(CN_nodes):
                        if ter.ConnectivityNode == CN.ID:
                            return  CN_nodes[index]

    print(current, current_ID, "no next node")
    return None


# Network Traversal
# The idea here is to implement an algorithmn that starts with a CN node, ending
# with either a CN, an end device, or an open breaker.

# The algorithmn will traverse through all of the CN node, and use each of the 
# CN node to build a conneciton path.





all_CE_stack = []
all_everything_stack = []
for CN_node in CN_nodes:
    
    previous_node = ''
    current_node = ''
    next_node = ''
    
    all_traversed = 0
    
    # Next, loop through the connected terminals, and build up a path
    for ter in CN_node.Terminal_list:
        
        CE_stack = []
        everything_stack = []
        
        current_node = CN_node
        everything_stack.append(current_node)
        
        # Check if the terminal has been traversed
        if ter.isTraversed == 1:
            
            all_traversed += 1
            
            # If all of the connected terminals have been traversed,
            # publish the list containing single CN_node into the all_everything list
            if all_traversed == CN_node.NoAttached:
                all_everything_stack.append(everything_stack)
                break
            
            continue
        
        next_node = find_next_node(previous_node, current_node)

        # Check what will become the next node
        while True:
            
            # If the current node is CN, the next node will be Terminal
            if current_node.node_type == 'ConnectivityNode':
                
                previous_node = current_node
                current_node = next_node
                next_node = find_next_node(previous_node, current_node)

            # If the current node is CE, then the next node will be Terminal
            elif current_node.node_type == 'ConductingEquipment':
                 
                CE_stack.append(current_node)
                everything_stack.append(current_node)
                previous_node = current_node
                current_node = next_node
                next_node = find_next_node(previous_node, current_node)
                
            # If the current node is terminal, then the next will be
            # CE or CN
            elif current_node.node_type == 'Terminal':
                
                everything_stack.append(current_node)
                
                #Register the traversed terminal
                current_node.isTraversed = 1
        
                # Register the traversed terminal in the terminal list of CE and CN nodes
                for ter_list_CE in CE_nodes:
                    for ter_CE in ter_list_CE.Terminal_list:
                        if current_node.ID == ter_CE.ID:
                            ter_CE.isTraversed = 1
                            
                for ter_list_CN in CN_nodes:
                    for ter_CN in ter_list_CN.Terminal_list:
                        if current_node.ID == ter_CN.ID:
                            ter_CN.isTraversed = 1
                            
                        
                # Check if the next node is either an open breaker, or an end device
                #print(type(next_node))
                #print(current_node.node_type)

                if next_node.node_type == 'ConductingEquipment':
                    
                    if next_node.CE_type == 'Breaker':
                        
                        isOpen = '' # If the breaker is opened
                            
                        for bk in Breaker_:
                            if bk.ID == next_node.ID:
                                if bk.opened == True:
                                    isOpen = True
                                    break
                                
                        # If the breaker is open, then terminate this loop
                        if isOpen == True:
                            break
                        
                        # If the breaker is not open, then move to the next node.
                        else:
                            
                            previous_node = current_node
                            current_node = next_node
                            next_node = find_next_node(previous_node, current_node)
                        
                    else:
                    
                        # If the CE is not a breaker, then check if it is an end device
                        if next_node.NoAttached == 1:
                            
                            # If yes, break this loop and register this end device
                            everything_stack.append(next_node)
                            CE_stack.append(next_node)
                            all_everything_stack.append(everything_stack)
                            all_CE_stack.append(CE_stack)
                            break
                    
                        else:
                            
                            # If it is not an end device, then continue to the next node                        
                            previous_node = current_node
                            current_node = next_node
                            next_node = find_next_node(previous_node, current_node)
                
                
                elif next_node.node_type == 'ConnectivityNode':
                    
                    # Register the CN node and break this loop
                    everything_stack.append(next_node)
                    all_everything_stack.append(everything_stack)
                    break
            
        
        previous_node = ''
        current_node = ''
        next_node = ''

# Get the type of all_everything_stack

all_everything_stack_type = []

for lst in range(len(all_everything_stack)):
    typ = []
    for index in range(len(all_everything_stack[lst])):
        
        if all_everything_stack[lst][index].node_type == 'ConductingEquipment':
            typ.append(all_everything_stack[lst][index].CE_type)
        
        else:
            typ.append(all_everything_stack[lst][index].node_type)
            
    all_everything_stack_type.append(typ)
    
# Create the relationship between busbar, end-device and CN using all_everything_stack
Busbar_CN = [] # Busbar - CN
CN_ED = [] # ED = End_Device
CN_CE_CN = [] # CE between two CN
CN_Busbar = {} # CN_Busbar dictionary. CN is ID and Busbar is busbar, not node 
CN_notAttached_Busbar = []
for path in all_everything_stack:
    
    if path[-1].node_type == 'ConductingEquipment' and len(path) == 3:
        
        if path[-1].CE_type == 'BusbarSection':
            Busbar_CN.append([path[-1], path[0]])
            
        else:
            CN_ED.append([path[0], path[-1]])
        
    elif path[-1].node_type == 'ConnectivityNode' and len(path) == 5:
        CN_CE_CN.append([path[-1], path[2], path[0]])

# CN_Busbar 
# CN attached to busbar
for path in Busbar_CN:
    
    BUS = ''
    for bs in BusbarSection_:
        if bs.ID == path[0].ID:
            CN_Busbar[path[1].ID] = bs
            
for cn in ConnectivityNode_:
    if cn.ID not in list(CN_Busbar.keys()):
        CN_notAttached_Busbar.append(cn)

# Create Panda Power network
network = pp.create_empty_network()

# Create buses. First, get the VoltageLevel and baseVoltage for each bus

for bb in BusbarSection_:
    for vl in VoltageLevel_:
        if vl.ID == bb.EquipmentContainer:
            bb.nominalVoltage = vl.name
            #print("vl", vl.name)

# Gather nominal voltage for CNs
for cn in ConnectivityNode_:
    for vl in VoltageLevel_:
        if vl.ID == cn.ConnectivityNodeContainer:
            cn.nominalVoltage = vl.name
    
# Create bus for each busbar
counter = 0
for BBS in BusbarSection_:
    BBS.pdbus = pp.create_bus(network, name = 'Node %s' % counter, vn_kv = float(BBS.nominalVoltage), type = 'b')
    counter+=1
# Create bus for each CN not attahced to busbar
for cn in CN_notAttached_Busbar:
    cn.pd_bus = pp.create_bus(network, name = 'Node %s' % counter, vn_kv = float(cn.nominalVoltage), type = 'n')
    counter+=1
# Register created bus with type b in the CNs attached to busbar
for cn in ConnectivityNode_:
    if cn.ID in list(CN_Busbar.keys()):
        cn.pd_bus = CN_Busbar[cn.ID].pdbus

# Create end devices

for path in all_everything_stack:
    
    temp_cn = ''
    for cn in ConnectivityNode_:
        if cn.ID == path[0].ID:
            temp_cn = cn.pd_bus
    
    if len(path) == 3:
        
        if path[-1].CE_type == 'LinearShuntCompensator':
            
            for sh in LinearShuntCompensator_:
                if sh.ID == path[-1].ID:
                    sh.pd_shunt = pp.create_shunt(network, temp_cn, p_mw = 0, q_mvar = -0.96, name = sh.name)
                    
        elif path[-1].CE_type == 'EnergyConsumer':
            
            for ec in EnergyConsumer_:
                if path[-1].ID == ec.ID:
                    ec.pd_EC = pp.create_load(network, temp_cn, p_mw = float(ec.p), q_mvar = float(ec.q), in_service = True, name = ec.name)
                             
        elif path[-1].CE_type == 'SynchronousMachine':
            
            for sm in SynchronousMachine_:
                if path[-1].ID == sm.ID:
                    sm.pd_gen = pp.create_gen(network, temp_cn, p_mw = -float(sm.p), vm_pu = float(sm.ratedU), max_q_mvar = -float(sm.maxQ), 
                                              min_q_mvar = -float(sm.minQ), in_service = True, name = sm.name)
                
        elif path[-1].CE_type == 'EnergySource':
                
            for ge in EnergySource_:
                if path[-1].ID == ge.ID:
                    ge.pd_gen = pp.create_sgen(network, temp_cn, p_mw = -float(ge.p), q_mvar = -float(ge.q),
                                                rx = float(ge.r))/float(ge.x)
                
                
# Transformers, Breakers and AC Lines
TID = 0
for path in all_everything_stack:
  
    temp_cn1 = ''
    temp_cn2 = ''
    hv = ''
    lv = ''
    
    if len(path) == 5:
        '''
        for index, p in enumerate(path):
            print(index, p.node_type)
        '''
    # Finding the buses correspoding to the CNs
 
        for cn in ConnectivityNode_:

            if cn.ID == path[0].ID:
                temp_cn1 = cn
                
            elif cn.ID == path[-1].ID:
                temp_cn2 = cn

        #print(temp_cn1,'\n',temp_cn2)
        
        if path[2].CE_type == 'PowerTransformer':
            
            if float(temp_cn1.nominalVoltage) > float(temp_cn2.nominalVoltage):
                hv = temp_cn1.pd_bus
                lv = temp_cn2.pd_bus
            else:
                lv = temp_cn1.pd_bus
                hv = temp_cn2.pd_bus

                
            for trans in PowerTransformer_:
                if trans.ID == path[2].ID:
                    #trans.pd_trans = pp.create_transformer(network, hv, lv, name = trans.name, std_type = '25 MVA 110/20 kV')
                    
                    if path[2].NoAttached == 2:
                        trans.pd_trans = pp.create_transformer(network, hv, lv, name = trans.name, std_type = '25 MVA 110/20 kV')
                    elif path[2].NoAttached == 3 and TID != path[2].ID:
                        TID = path[2].ID
                        hv = 12
                        mv = 2
                        lv = 11
                        trans.pd_trans = pp.create_transformer3w(network, hv, mv, lv, name = trans.name, std_type = '63/25/38 MVA 110/20/10 kV')
                    elif path[2].NoAttached == 3 and TID == path[2].ID:
                        continue
                    break
        
        elif path[2].CE_type == 'Breaker':
            
            for cb in Breaker_:
                if cb.ID == path[2].ID:
                    cb.pd_cb = pp.create_switch(network, temp_cn1.pd_bus, temp_cn2.pd_bus, et = 'b', type = 'CB', name = cb.name)
            
        elif path[2].CE_type == 'ACLineSegment':
            
            for line in ACLineSegment_:
                if line.ID == path[2].ID:
                    line.pd_line = pp.create_line(network, temp_cn1.pd_bus, temp_cn2.pd_bus, length_km = 10, name = line.name, std_type = '48-AL1/8-ST1A 20.0')
  
#pp.plotting.simple_plot(network)

if selection == "1":
    graph_name = 'Assignment_system.html'
else:
    graph_name = 'test_system.html'

pp.plotting.to_html(network, graph_name)
webbrowser.open(graph_name, new=2)
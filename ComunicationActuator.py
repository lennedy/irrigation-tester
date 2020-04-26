from Comunication import *

class Relay:
  def __init__(self):
    self.value = False


class Valve:

    def __init__(self, pin: int, name, active_high: bool = False, active_open: bool = True):
        self.active_open = active_open
        initial_value = not active_open  # initially closed
        if(pin<0):
          self._relay = Relay()
        else:
          self._relay = DigitalOutputDevice(pin=pin, active_high=active_high, initial_value=initial_value)

        self.name = name

    def open(self):
        self._relay.value = self.active_open

    def close(self):
        self._relay.value = not self.active_open

    @property
    def is_open(self) -> bool:
        if self.active_open:
            return self._relay.value
        else:
            return not self._relay.value

    @property
    def is_closed(self):
        return not self.is_open

    def getName(self):
        return self.name

    def setValue(self, value:bool):
        self._relay.value = value

    def getValue(self):
        return self._relay.value

    def print(self):
        print ("Nome: "+self.name)
        print ("Value: "+self.active_open)

class ComunicationActuator(Comunication):
  global valves
  global pumps
  global automatic

#########################################################################################

  def __init__(self):
    self.valves = []
    self.pumps = []
    self.automatic = False

#########################################################################################

  def __getitem__(self, index):
    for x in self.valves:
      if (x.getName() == index):
        return x.getValue()
    return False

#########################################################################################

  def __setitem__(self, index, value):
    for x in self.valves:
      if (x.getName() == index):
        x.setValue(value)
        return True
    for x in self.pumps:
      if (x.getName() == index):
        x.setValue(value)
        return True

    return False

#########################################################################################
  def updateAtomatic(self, automatic):
    self.automatic = automatic
#########################################################################################

  def addValv(self, valve):
    self.valves.append( valve )

#########################################################################################

  def addPump(self, pump):
    self.pumps.append( pump )

#########################################################################################

  def updateActuatorsInServer(self):
    valve_val = []
    pump_val = []
    for valv in self.valves:
      valve_val.append( {"id":valv.getName(), "isOpen":valv._relay.value} )
    for pump in self.pumps:
      pump_val.append( {"id":pump.getName(), "isOpen":pump._relay.value} )

    payload = {"automatic" : self.automatic,
               "pumps": pump_val,
               "valves": valve_val}

    self.send_pump_valve_value(payload)

#########################################################################################

  def getDataInServer(self):
    valve_val = []
    pump_val = []

    for valv in self.valves:
      valve_val.append( {"id":valv.getName(), "isOpen":valv._relay.value} )
    for pump in self.pumps:
      pump_val.append( {"id":pump.getName(), "isOpen":pump._relay.value} )

    payload = {"pumps": pump_val,
               "valves": valve_val}


    response = self.get_pump_valve_value()
    obj = json.loads(response)

    pump_instructions = obj["pumps"]
    valve_instructions = obj["valves"]

#    print(pump_instructions)
#    print(valve_instructions)

    self.automatic  = obj["automatic"]

    for n in valve_instructions:
      self[n] = valve_instructions[n]
#      print(n)
#      print(self[n])
    for n in pump_instructions:
      self[n] = pump_instructions[n]

    
#########################################################################################

  def update(self):

    pump_values = {}
    valve_values = {}


    payload = {"moisture": {},
               "temperature": {},
               "tanks": {},
               "pumps": {},
               "valves": {}}

    self.send_and_get_instructions(payload)


#########################################################################################

  def getAutomatic(self):
    return self.automatic

#########################################################################################

#c = ComunicationActuator()

#c.addValv( Valve(-1,"valv1") )
#c.addValv( Valve(-1,"valv2") )
#c.addValv( Valve(-1,"valv3") )

#c["valv1"] = False

#print(c["valv1"])
#c.updateActuatorsInServer()








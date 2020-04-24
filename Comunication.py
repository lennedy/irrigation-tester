import json
import logging
from pprint import pformat
import requests

# Web Service endpoint
service_base_url = "http://localhost:8080/api/"

#Criacao de log
logging.basicConfig(format='%(asctime)s %(levelname)s\t%(message)s', level=logging.WARNING)
logger = logging.getLogger('oh-balcony')
logger.setLevel(logging.INFO)



class Comunication:

#########################################################################################

  def get_service_endpoint(self, endpoint):
      if service_base_url.endswith("/"):
          return service_base_url + endpoint
      else:
          return service_base_url + "/" + endpoint


#########################################################################################

  def send_and_get_instructions(self, payload):
      headers = {'content-type': 'application/json'}
      instructions = {"pumps": {}, "valves": {}}  # default: all off/closed
      controller_name = "controller1"
      try:
        response = requests.post(self.get_service_endpoint("updateControllerState/" + controller_name), data=json.dumps(payload), headers=headers, timeout=5.0)
        response.raise_for_status()

        instructions = response.json()
      except:
        logger.exception("Communication error with server")
      return instructions

#########################################################################################

  def send_pump_valve_value(self, payload):
    headers = {'content-type': 'application/json'}

    try:
##      logger.info("Pump e Valve: " + pformat(payload))
      response = requests.post(self.get_service_endpoint("updateActuators"), data=json.dumps(payload), headers=headers, timeout=5.0)
      response.raise_for_status()
      logger.info(pformat(payload))
    except:
      logger.exception("Communication error with server")

#########################################################################################

  def get_pump_valve_value(self):
    headers = {'content-type': 'application/json'}
    payload = ""
    try:
##      logger.info("Pump e Valve: " + pformat(payload))
      response = requests.get(self.get_service_endpoint("valves"), data=json.dumps(payload), headers=headers, timeout=5.0)
      response.raise_for_status()
      return response.text
      #logger.info(pformat(payload))
    except:
      logger.exception("Communication error with server")

#########################################################################################

#com = Comunication()

#pump_val = [{"id":"pump1", "isActive":False} ]
#valve_val = [{"id":"valv1", "isOpen":False}, {"id":"valv2", "isOpen":True} ]

#pl = {"pumps": pump_val,
 #   "valves": valve_val}

#com.send_pump_valve_value(pl)


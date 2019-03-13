import numpy as np

from communication.arduino_link import ArduinoLink
from communication.xbee_link import XBeeLink
from pso.data import PSOData, Coordinates, Reading
from util import get_config

# Data class representing a bot
class BotData():


    def __init__(self, id):
        # Add more variables as needed
        self.id = id

        # Will be synced with arduino
        self.cur_gps_x = 0
        self.cur_gps_y = 0
        self.cur_reading = Reading(0)


# Overall bot "hub" - holds all of a bot's components
class NavSwarmBot:


    def __init__(self):
        self.config = get_config()
        self.bot_data = BotData(self.retrieve_bot_id())
        self.pso_data = PSOData()
        #self.arduino = ArduinoLink(self.data, self.config["arduino"])
        self.xbee = XBeeLink(self.bot_data, self.config["xbee"])

    # TODO : make the bot communicate with the other bots to get a unique ID
    def retrieve_bot_id(self):
        return 0
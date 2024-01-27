#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from time import sleep

class Ears():

    def __init__(self):
        self.logger = logging.getLogger("EARS")
        self.logger.info("Initializing EARS Thread ...")

    def birth(self):
        self.logger.info("... wiggling ears")
        while True:
            self.logger.info("... running wild!")
            sleep(5)

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from time import sleep

class Ears():

    def __init__(self):
        self.logger = logging.getLogger("EARS")
        self.logger.info("[#] Initializing EARS Thread ...")

    def birth(self):
        while True:
            self.logger.info("... running wild with ears movement!")
            sleep(5)

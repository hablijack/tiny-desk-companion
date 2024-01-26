#!/usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import logging


class Ears():

    async def __init__(self):
        self.logger = logging.getLogger("EARS")
        self.logger.info("Initializing EARS Thread ...")
        while True:
            self.logger.debug("... running wild!")
            await asyncio.sleep(1)

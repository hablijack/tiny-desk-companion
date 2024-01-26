#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from body_parts.eyes import Eyes


class Deskrobot():
    
    def __init__(self):
        self.logger = logging.getLogger('DESKROBOT')
        self.logger.debug('... initializing deskrobot system, press Ctrl-C to quit!')
        Eyes()

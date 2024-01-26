#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from tornado import gen
from body_parts.eyes import Eyes


class Deskrobot():

    def __init__(self):
        self.logger = logging.getLogger('BLUEBERRY')
        self.logger.debug('... initializing blueberry system, press Ctrl-C to quit!')
        self.init_eyes()

    @gen.coroutine
    def init_eyes(self):
        self.logger.debug('... initializing eyes to display on oled-screen')
        Eyes()
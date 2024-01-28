
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from body_parts.eyes import Eyes
from body_parts.ears import Ears
from multiprocessing import Process


class Deskrobot():
    def __init__(self):
        self.logger = logging.getLogger('DESKROBOT')
        self.eyes = Eyes()
        self.ears = Ears()

    def birth(self):
        self.logger.info('[#] Initializing deskrobot system, press Ctrl-C to quit!')
        Process(target=self.eyes.birth).start()
        Process(target=self.ears.birth).start()

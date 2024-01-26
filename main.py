#!/usr/bin/python3
# -*- coding: utf-8 -*-

import signal
import sys
import logging
from deskrobot import Deskrobot
import asyncio

def signal_handler(signal, frame):
  sys.exit(0)

if __name__ in '__main__':

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s [%(name)s] %(message)s",
        datefmt='%d.%m.%Y %H:%M:%S',
        handlers=[
            logging.FileHandler("log/debug.log"),
            logging.StreamHandler()
        ]
    )
    signal.signal(signal.SIGINT, signal_handler)
    asyncio.run(Deskrobot())

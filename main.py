#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import tornado
from ui.webserver import WebServer
from deskrobot import Deskrobot


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
    deskrobot = Deskrobot()
    WebServer().serve()
    tornado.ioloop.IOLoop.current().start()
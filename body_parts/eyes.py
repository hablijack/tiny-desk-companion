#!/usr/bin/python3
# -*- coding: utf-8 -*-

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep, time
from random import randint, uniform
import logging
import asyncio


class Eyes():

    serial = i2c(port=1, address=0x3C)
    device = sh1106(serial)
    position = dict(left=25, top=10)
    eye = dict(state='default', x='center', y='center')

    async def __init__(self):
        self.logger = logging.getLogger("EYES")
        self.logger.info("Initializing EYES Thread ...")
        while True:
            state = randint(0,1)
            if state == 0:
                self.eye['state'] = 'default'
            elif state == 1:
                self.eye['state'] = 'blink'

            direction = randint(0,8)
            if direction == 0:
                self.eye['x'] = 'center'
                self.eye['y'] = 'center'
            elif direction == 1:
                self.eye['x'] = 'left'
                self.eye['y'] = 'center'
            elif direction == 2:
                self.eye['x'] = 'right'
                self.eye['y'] = 'center'
            elif direction == 3:
                self.eye['x'] = 'center'
                self.eye['y'] = 'top'
            elif direction == 4:
                self.eye['x'] = 'left'
                self.eye['y'] = 'top'
            elif direction == 5:
                self.eye['x'] = 'right'
                self.eye['y'] = 'top'
            elif direction == 6:
                self.eye['x'] = 'center'
                self.eye['y'] = 'bottom'
            elif direction == 7:
                self.eye['x'] = 'left'
                self.eye['y'] = 'bottom'
            elif direction == 8:
                self.eye['x'] = 'right'
                self.eye['y'] = 'bottom'

            state = randint(0,1)
            if state == 0:
                self.eye['state'] = 'default'
                await self.default(self.eye, self.position)
            elif state == 1:
                self.eye['state'] = 'blink'
                await self.blink(self.eye, self.position)

    async def draw_rounded(self, left, top, width, height, space, radius, offset):
        with canvas(self.device) as draw:
            draw.rounded_rectangle((left,                 top + offset, left + width,                 height + top + offset), fill="white", radius=radius)
            draw.rounded_rectangle((left + width + space, top + offset, left + width + space + width, height + top + offset), fill="white", radius=radius)

    async def look_around(self, eye, pos):
        match eye['x']:
            case 'center':
                if pos['left'] < 25:
                    pos['left'] += 1
                elif pos['left'] > 25:
                    pos['left'] -=1
            case 'left':
                if pos['left'] > 0:
                    pos['left'] -= 1
            case 'right':
                if pos['left'] < 50:
                    pos['left'] += 1

        match eye['y']:
            case 'center':
                if pos['top'] < 15:
                    pos['top'] += 1
                elif pos['top'] > 15:
                    pos['top'] -= 1
            case 'top':
                if pos['top'] > 0:
                    pos['top'] -= 1
            case 'bottom':
                if pos['top'] < 25:
                    pos['top'] += 1

    async def default(self, eye, pos):
        duration_ms = uniform(1.0, 5.0)
        future_timestamp = time() + duration_ms
        while time() < future_timestamp:
            self.draw_rounded(pos['left'], pos['top'], 30, 35, 10, 9, 0)
            self.look_around(eye, pos)

    async def blink(self, eye, pos):
        self.draw_rounded(pos['left'], pos['top'], 30, 5, 10, 9, 20)
        await asyncio.sleep(0.1)

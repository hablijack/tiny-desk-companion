from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep, time
from random import randint, uniform

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

position = dict(left=25, top=10)

eye = dict(state='default', x='center', y='center')

def draw_rounded(left, top, width, height, space, radius, offset):
    with canvas(device) as draw:
        draw.rounded_rectangle((left,                 top + offset, left + width,                 height + top + offset), fill="white", radius=radius)
        draw.rounded_rectangle((left + width + space, top + offset, left + width + space + width, height + top + offset), fill="white", radius=radius)

def look_around(eye, pos):
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

def default(eye, pos):
    duration_ms = uniform(1.0, 5.0)
    future_timestamp = time() + duration_ms
    while time() < future_timestamp:
        draw_rounded(pos['left'], pos['top'], 30, 35, 10, 9, 0)
        look_around(eye, pos)

def blink(eye, pos):
    draw_rounded(pos['left'], pos['top'], 30, 5, 10, 9, 20)
    sleep(0.1)

while True:
    state = randint(0,1)
    if state == 0:
        eye['state'] = 'default'
    elif state == 1:
        eye['state'] = 'blink'

    direction = randint(0,8)
    if direction == 0:
        eye['x'] = 'center'
        eye['y'] = 'center'
    elif direction == 1:
        eye['x'] = 'left'
        eye['y'] = 'center'
    elif direction == 2:
        eye['x'] = 'right'
        eye['y'] = 'center'
    elif direction == 3:
        eye['x'] = 'center'
        eye['y'] = 'top'
    elif direction == 4:
        eye['x'] = 'left'
        eye['y'] = 'top'
    elif direction == 5:
        eye['x'] = 'right'
        eye['y'] = 'top'
    elif direction == 6:
        eye['x'] = 'center'
        eye['y'] = 'bottom'
    elif direction == 7:
        eye['x'] = 'left'
        eye['y'] = 'bottom'
    elif direction == 8:
        eye['x'] = 'right'
        eye['y'] = 'bottom'

    state = randint(0,1)
    if state == 0:
        eye['state'] = 'default'
        default(eye, position)
    elif state == 1:
        eye['state'] = 'blink'
        blink(eye, position)

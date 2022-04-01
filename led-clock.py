#!/usr/bin/python3
from smbus import SMBus

import datetime
t = datetime.datetime.now().time()
print(t)

d=(0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f)
m=SMBus(1)
m.write_byte(0x24, 0x11)
m.write_byte(0x34, d[int(t.hour / 10)])
m.write_byte(0x35, d[int(t.hour % 10)])
m.write_byte(0x36, d[int(t.minute / 10)])
m.write_byte(0x37, d[int(t.minute % 10)])

from WeDo2 import *
from bleak import BleakClient
import asyncio

h = HubManager(1)

# h.wedos[0].set_led_mode(LED_DISCREET_MODE)

for i in range(10):
	print('INDEX: ' + str(i))	
	h.wedos[0].set_led_color(i)
	asyncio.sleep(5)

# while True:
# 	asyncio.sleep(1)
# h.wedos[0].set_led_color(255,0,0)

# loop = asyncio.get_event_loop()

# async def run():
# 	await BleakClient(address='24:71:89:17:9D:AE', loop=loop).connect()

# loop.run_until_complete(run())
#!/usr/bin/python2

from multiprocessing import Process
from time import sleep
from cfg import *
import argparse

class Wiimote(cwiid.Wiimote, Process):
    LED_CYCLE = (1, 3, 7, 15, 14, 12, 8, 0)

    def __init__(self, controller_num, config=None):
        Process.__init__(self)
        self.controller_num = controller_num
        if controller_num == 1:
            self.led_cycle = self.LED_CYCLE
        elif controller_num == 2:
            self.led_cycle = self.LED_CYCLE[::-1]
        self.active_config = config or pointed_global
        inputs = []
        for event in self.active_config.event_list:
            inputs.append(event.uinput_event)
        self.device = uinput.Device(inputs)

    def run(self):
        cwiid.Wiimote.__init__(self)
        self.rpt_mode = cwiid.RPT_ACC | cwiid.RPT_BTN | cwiid.RPT_EXT | cwiid.RPT_IR | cwiid.RPT_STATUS
        sleep(1)
        wm.rumble = 1
        sleep(0.1)
        wm.rumble = 0
        x = 0
        led = 0
        while True:
            sleep(0.001)
            if x in range(0, 1001, 125): # every 1/8th second
                self.led = self.led_cycle[led]
                led += 1
            if x in range(0, 1001, 10): # every 1/100th second
                for event in self.active_config.event_list:
                    event(self.state, self.device)
            x += 1
            if led >= len(self.led_cycle):
                led = 0
            if x >= 1000:
                x = 0

if __name__ == '__main__': # need to modify this to accept args from the command line
    parser = argparse.ArgumentParser(description='wii-script')
    parser.add_argument('-p', action='store', dest='player', type=int,
                        help='Number of player/wiimote to connect',
                        default=1)
    parser.add_argument('-c', action='store', dest='config',
                        help='config to load', default='pointed_global')
    results = parser.parse_args()
    exec('config = %s' % results.config)
    wm = Wiimote(results.player, config)
    wm.run()
    # one day it might work like this...
    #for x in range(1, results.players+1):
    #    wm = Wiimote(x, configs[results.config])
    #    wm.start()
    while True:
        sleep(1)

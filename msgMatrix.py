#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Commandline Wrapper
# Thomas Wenzlaff
# See LICENSE.rst for details.

import time, argparse, os
import argparse
from datetime import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
#from getIP import getIP
#from sftpStatus import checkSFTP
#from dotenv import load_dotenv

#load_dotenv()

#sftpServer   = os.environ.get('sftpURLEdited')
#sftpUser     = os.environ.get('sftpUserEdited')
#sftpPassword = os.environ.get('sftpPassEdited')



def output(n, block_orientation, rotate, inreverse, text):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)

    show_message(device, text, fill="white", font=proportional(CP437_FONT), scroll_delay=0.05)
    time.sleep(1)


def outputSlow(n, block_orientation, rotate, inreverse, text):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)

    show_message(device, text, fill="white", font=proportional(CP437_FONT), scroll_delay=0.025)
    time.sleep(1)


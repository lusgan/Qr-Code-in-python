# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:41:25 2023

@author: balbi
"""

import qrcode

link = qrcode.make("https://github.com/lusgan")

link.save("Qrcode_link.png")
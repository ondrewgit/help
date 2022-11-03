#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

fn = sys.argv[1]
if os.path.exists(fn):
    print(os.path.basename(fn)+" Exists")
    # file exists



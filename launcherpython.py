#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:04:11 2019

@author: rogerslc
"""
import sys
import os

from time import sleep
#cwd = os.getcwd()


counterscript = '/n/holylfs02/LABS/guenette_lab/users/lrogers/otherJob.sh'
script        = sys.argv[1] #'SearchingForXe137andNeutrons.py'
p1            = sys.argv[2] #files to process location
p2            = sys.argv[3] #where to save
min_filenum   = sys.argv[4]
numoffiles    = sys.argv[5]
batchsize     = int(sys.argv[6])

path_params = '--export=script='+script+',p1='+p1+',p2='+p2+','

for i in range(int(min_filenum), int(numoffiles), batchsize):
    max_launch = i + batchsize

    params = path_params + 'min='+str(i)+',max='+str(max_launch)
    cmd = 'sbatch ' + params + ' ' + counterscript

    os.system(cmd)
    sleep(0.5)

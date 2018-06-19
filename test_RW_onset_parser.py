#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created May 2018
@author: JRS, script kiddie from gracer
"""

#!/usr/bin/python
#get onsets

import numpy
import os
import pdb
import glob

handles=[]

basepath='/Users/jennygilbert/Documents/RW_bevel/test_log'
os.chdir(basepath)


ignore = ['DATA 	Keypress: o','Level post injecting via pump at address']


#get the global info about the run. 
for file in glob.glob(os.path.join(basepath,'bevel*.log')):
    print(file)

    sub=file.split('/')[6].split('_')[1]
    run=file.split('/')[6].split('_')[2]
    print([sub,run])
    
#   open the script and read in log data
    with open(file,'r') as infile:
    stim=[]
        response=[]
        
        for x in infile.readlines():
            if x.find('position')>-1:
                l_s=x.strip().split('\t')
                stim=(l_s[1])
                print(stim)
            if x.find('Keypress:')>-1:
                l_s=x.strip().split('\t')
                response=(l_s[2])
                print(response)
            if x.find('Key Press Missed')>-1:
                l_s=x.strip().split('\t')
                response=(l_s[1])
                print(response)
        except KeyError:
            pass  

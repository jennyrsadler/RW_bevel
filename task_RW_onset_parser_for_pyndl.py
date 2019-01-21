#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:21:45 2018

@author: jennygilbert

This script is used to conver the log files from the probabilistic reward learning task in BeveL to csv files formatted for Rescorla Wagner modeling in pyndl.

- pyndl requires a single file per participant with 2 columns: cue & outcome. Each row represents one event. 
    - In our paradigm, the chosen shape is the cue, and the taste delivered is the outcome
    - The script will pull the shape selected (A, B, C, D, E,or F) and the taste delivered (sweet or bitter) on each trial
    
"""
import os
import glob
import pandas as pd

handles=[]

basepath='/Users/jennygilbert/Documents/RW_bevel/task_logs'
os.chdir(basepath)


ignore = ['DATA 	Keypress: o','Level post injecting via pump at address']

for file in glob.glob(os.path.join(basepath,'bevel_*.log')):
    print(file)

    sub=file.split('/')[6].split('_')[1]
    run=file.split('/')[6].split('_')[2]
    print([sub,run])
    

    with open(file,'r') as infile:
        cue=[]
        outcome=[]
        start_time=None
        
        for x in infile.readlines():    
            if not x.find(ignore[0])>-1 or x.find(ignore[1])>-1:
                l_s=x.strip().split()
                
                if x.find('Level injecting via pump at address ')>-1:#find the tasty image
                    l_s=x.strip().split()
                    #print(l_s)
                    if l_s[7] == '1' and l_s[16] == 'a.jpg':
                        cue.append('A')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'c.jpg':
                        cue.append('C')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'e.jpg':
                        cue.append('E')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'b.jpg':
                        cue.append('B')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'd.jpg':
                        cue.append('D')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'f.jpg': 
                        cue.append('F')
                        outcome.append('Sweet')
                    if l_s[7] == '2' and l_s[16] == 'b.jpg':
                        cue.append('B')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'd.jpg':  
                        cue.append('D')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'f.jpg':
                        cue.append('F')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'a.jpg':
                        cue.append('A')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'c.jpg':
                        cue.append('C')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'e.jpg':
                        cue.append('E')
                        outcome.append('Bitter')

                if x.find('Key Press Missed!')>-1:
                    l_s=x.strip().split()
                    #print(l_s)
                    cue.append('Miss')
                    outcome.append('Miss')
                

        #files2make=['task_log.csv']
        #mydict={}
        #try:
      #      for files in files2make:
    path='%s_%s_nBayesDM.txt'%(sub,run)
    print(path)
    print(sub)
                #if os.path.exists(path) == True:
                    #print ('exists')
                    #break
     #           else:
      #              mydict[files] = path
           
    f_make=open(path, 'w')
    for a,b in zip(cue,outcome):
        f_make.write(str(a)+'\t'+str(b)+'\n')
    f_make.close()


        

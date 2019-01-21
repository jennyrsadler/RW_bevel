#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:21:45 2018

@author: jennygilbert
"""

import numpy
import os
import pdb
import glob

handles=[]

basepath='/Users/jennygilbert/Documents/RW_bevel/task_logs'
os.chdir(basepath)


ignore = ['DATA 	Keypress: o','Level post injecting via pump at address']

#files = [file for file in os.listdir(".") if (file.lower().endswith('.log'))]
#files.sort(key=os.path.getmtime)

#get the global info about the run. 
for file in glob.glob(os.path.join(basepath,'bevel_*.log')):
    print(file)

    sub=file.split('/')[6].split('_')[1]
    run=file.split('/')[6].split('_')[2]
    print([sub,run])
    
#   open the script and read in log data
    with open(file,'r') as infile:
        stim=[]
        response=[]
        outcome=[]
        PE=[]
        RT=[]
        start_time=None
        
        for x in infile.readlines():
#            if x.find('Keypress: q'):
#                continue
            
            if not x.find(ignore[0])>-1 or x.find(ignore[1])>-1:
                l_s=x.strip().split()
               # print l_s
                
                if x.find('Level start key press')>-1:#find the start
                    l_s=x.strip().split()
                    start_time=float(l_s[0])
                
                if x.find('position')>-1:
                    l_s=x.strip().split()
                    #print(l_s)                    
                    if l_s[2] == 'a.jpg' or l_s[2] == 'b.jpg':
                        stim.append('AB')
                    if l_s[2] == 'c.jpg' or l_s[2] == 'd.jpg':
                        stim.append('CD')
                    if l_s[2] == 'e.jpg' or l_s[2] == 'f.jpg':
                        stim.append('EF')
                 #       print(stim)
                        
                if x.find('at time')>-1:
                    l_s=x.strip().split()
                    RT.append(l_s[5])
                    
                if x.find('Level injecting via pump at address ')>-1:#find the tasty image
                    l_s=x.strip().split()
                    #print(l_s)
                    if l_s[7] == '1' and l_s[16] == 'a.jpg':
                        PE.append('No')
                        response.append('A')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'c.jpg':
                        PE.append('No')       
                        response.append('C')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'e.jpg':
                        PE.append('No')
                        response.append('E')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'b.jpg':
                        PE.append('Positive PE')
                        response.append('B')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'd.jpg':
                        PE.append('Positive PE')
                        response.append('D')
                        outcome.append('Sweet')
                    if l_s[7] == '1' and l_s[16] == 'f.jpg':
                        PE.append('Positive PE')   
                        response.append('F')
                        outcome.append('Sweet')
                    if l_s[7] == '2' and l_s[16] == 'b.jpg':
                        PE.append('No')
                        response.append('B')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'd.jpg':
                        PE.append('No')      
                        response.append('D')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'f.jpg':
                        PE.append('No')
                        response.append('F')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'a.jpg':
                        PE.append('Negative PE')
                        response.append('A')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'c.jpg':
                        PE.append('Negative PE')
                        response.append('C')
                        outcome.append('Bitter')
                    if l_s[7] == '2' and l_s[16] == 'e.jpg':
                        PE.append('Negative PE')
                        response.append('E')
                        outcome.append('Bitter')

                if x.find('Key Press Missed!')>-1:
                    l_s=x.strip().split()
                    #print(l_s)
                    response.append('Miss')
                    PE.append('N/A')
                    RT.append('N/A')
                    outcome.append('N/A')
                

        #files2make=['task_log.csv']
        #mydict={}
        #try:
      #      for files in files2make:
    path='%s_task_log_%s.csv'%(sub,run)
    print(path)
    print(sub)
                #if os.path.exists(path) == True:
                    #print ('exists')
                    #break
     #           else:
      #              mydict[files] = path
           
    f_make=open(path, 'w')
    for a,b,c,d,e in zip(stim,response,outcome,PE,RT):
        f_make.write(str(a)+','+str(b)+','+str(c)+','+str(d)+','+str(e)+'\n')
    f_make.close()
            
#        except KeyError:
#            pass   
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
                print l_s
                
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
                        print(stim)
                        
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
                
#Combine into one log file for the run. 






####OLD                  
       # sweet_expected_onset=(numpy.asarray(sweet_expected_onset,dtype=float))-start_time
       # sweet_PE_onset=(numpy.asarray(sweet_PE_onset,dtype=float))-start_time
       # bitter_expected_onset=(numpy.asarray(bitter_expected_onset,dtype=float))-start_time
       # bitter_PE_onset=(numpy.asarray(bitter_PE_onset,dtype=float))-start_time
       # AB_img_onsets=(numpy.asarray(AB_img_onsets,dtype=float))-start_time 
       # CD_img_onsets=(numpy.asarray(CD_img_onsets,dtype=float))-start_time 
       # EF_img_onsets=(numpy.asarray(EF_img_onsets,dtype=float))-start_time 
       # RT_onsets=(numpy.asanyarray(RT_onsets,dtype=float))-start_time
       # files2make=['neu','sweet','bitter','sweet_expected','sweet_PE','bitter_expected','bitter_PE', 'img', 'AB', 'CD', 'EF','RT']
        files2make=['neu','sweet','bitter','img','performance']
        mydict={}
        try:
            for files in files2make:
                path='/Users/jennygilbert/Desktop/onsets/%s_%s_%s.txt'%(sub,files,run)
                if os.path.exists(path) == True:
                    print ('exists')
                    break
                else:
                    mydict[files] = path
            f_neu=open(mydict['neu'], 'w')
            for t in range(len(neu_onsets)):
                f_neu.write('%f\t2\t1\n'%(neu_onsets[t]))
            f_neu.close()
            
            f_sweet=open(mydict['sweet'], 'w')
            for t in range(len(sweet_onsets)):
                f_sweet.write('%f\t5\t1\n' %(sweet_onsets[t]))
            f_sweet.close()
            
            f_bitter=open(mydict['bitter'], 'w')
            for t in range(len(bitter_onsets)):
                f_bitter.write('%f\t5\t1\n' %(bitter_onsets[t]))
            f_bitter.close()

           # f_sweet_exp=open(mydict['sweet_expected'], 'w')
           # for t in range(len(sweet_expected_onset)):
           #     f_sweet_exp.write('%f\t5\t1\n' %(sweet_expected_onset[t]))
           # f_sweet_exp.close()

           # f_sweet_PE=open(mydict['sweet_PE'], 'w')
           # for t in range(len(sweet_PE_onset)):
           #     f_sweet_PE.write('%f\t5\t1\n' %(sweet_PE_onset[t]))
           # f_sweet_PE.close()                   

           # f_bitter_exp=open(mydict['bitter_expected'], 'w')
           # for t in range(len(bitter_expected_onset)):
           #     f_bitter_exp.write('%f\t5\t1\n' %(bitter_expected_onset[t]))
           # f_bitter_exp.close()            

           # f_bitter_PE=open(mydict['bitter_PE'], 'w')
           # for t in range(len(bitter_PE_onset)):
           #     f_bitter_PE.write('%f\t5\t1\n' %(bitter_PE_onset[t]))
           # f_bitter_PE.close()  

            f_img=open(mydict['img'], 'w')
            for t in range(len(img_onsets)):
                f_img.write('%f\t2\t1\n' %(img_onsets[t]))
            f_img.close()              

            f_performance=open(mydict['performance'], 'w')
            for t in range(len(performance)):
                f_performance.write('%s\n' %(performance[t]))
            f_performance.close() 

            # f_AB=open(mydict['AB'], 'w')
           # for t in range(len(AB_img_onsets)):
           #     f_AB.write('%f\t2\t1\n' %(AB_img_onsets[t]))
           # f_AB.close()  

          #  f_CD=open(mydict['CD'], 'w')
          #  for t in range(len(CD_img_onsets)):
          #      f_CD.write('%f\t2\t1\n' %(CD_img_onsets[t]))
          #  f_CD.close()  

          #  f_EF=open(mydict['EF'], 'w')
          #  for t in range(len(EF_img_onsets)):
          #      f_EF.write('%f\t2\t1\n' %(EF_img_onsets[t]))
          #  f_EF.close()  
            
           # f_RT=open(mydict['RT'], 'w')
           # for t in range(len(RT_onsets)):
           #     f_RT.write('%f\n' %(RT_onsets[t]))
           # f_RT.close()

        except KeyError:
            pass   
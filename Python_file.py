#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:40:55 2019

@author: varenyarao
"""
#HW1 Question 2
#By Varenya Rao
#UNI - vr2456

file= open('question4.txt','r')
s=file.read()
file.close()
s=s.lower()
wordlist = s.split("\n")
wordlist = s.split()
wordlist
frequency = {}
for item in wordlist:
    if (item in frequency):
        frequency[item] += 1
    else: 
        frequency[item] = 1

Final_list = sorted(frequency.items() , reverse=True, key=lambda x: x[1])
f=open("final_ouput.txt", "w")
for elem in Final_list :
    print(elem[0]," ",elem[1], file=f)
f.close()
    

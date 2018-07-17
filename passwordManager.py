#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 23:11:44 2017

@author: utshrivastav
"""

import pyperclip

passwords = {'gmail':'pass','facebook':'pass','UF':'pass'}
account = input('Enter the website of which you want to copy password of :\n')
if account in passwords.keys():
    pyperclip.copy(passwords[account])
    print('Password of '+account+' is copied')
else:
    print('this website is not in the system, please contact the administrator')
    
    

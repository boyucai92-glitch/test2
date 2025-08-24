#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 20:11:08 2025

@author: a0955779017
"""
print("*")
x = 1
for i in range(1, 21):
    x=2+x
    for j in range(x):
        print("*", end="")   # 不換行印出
    print()  # 換行



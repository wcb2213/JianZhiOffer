#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/10

import sys_test


a1=sys_test.stdin.readline().strip()
## b str 1 2 3
n, d = map(int,a1.split())
l1, l2 = [], []
for i in range(n):
    a2 = list(map(int, sys_test.stdin.readline().strip().split()))
    l1.append(a2[0])
    l2.append(a2[1])
max = 0
l2.max
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:06:02 2019

@author: Isaiah
"""
#The purpose of this script is to be able to determine what are the key words
#commonly mentioned in job posting that I am interested in applying to.
#
#Influence was taken from the following link:
#    https://stackoverflow.com/questions/10390989/python-program-that-finds-
#    most-frequent-word-in-a-txt-file-must-print-word-and

import re
from collections import Counter

#
with open('GD_JobPosting.txt') as f:
    passage = f.read()
#
words = re.findall(r'\w+', passage)
#
cap_words = [word.upper() for word in words]
#
word_counts = Counter(cap_words)















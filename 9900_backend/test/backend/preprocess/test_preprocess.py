#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:06:24 2019

@author: hal
"""

from preprocess import construct_corpus

chunks_corpus_raw = []
with open('answer_content.txt') as f:
    for line in f:
        chunks_corpus_raw.append(line.splitlines()[0])
    
chunks_corpus = construct_corpus(chunks_corpus_raw)
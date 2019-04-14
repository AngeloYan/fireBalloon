#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:48:56 2019

@author: hal
"""

import numpy as np

def load_data(index):
    if index == 'corpus_data':
        corpus_data = np.load('9900_backend/corpus_data.npy')
        corpus_data = list(corpus_data)
        return corpus_data
    elif index == 'query_data':
        query_data = np.load('query_data.npy')
        query_data = list(query_data)[0]
        return query_data
    elif index == 'result_index':
        result_index = np.load('result_index.npy')
        result_index = list(result_index)[0]
        return result_index
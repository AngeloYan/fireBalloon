#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:23:55 2019

@author: hal
"""

#from keywords_extraction import keywords_extracted_tfidf
from preprocess import construct_corpus
from load_data import load_data
import numpy as np
import math




def ir_model(query):
    
    query = query
    
    #corpus_sorted, features, idf, vocabulary, length_corpus, chunks_corpus_raw, title_corpus_raw, learning_factor = keywords_extracted_tfidf()
    corpus_sorted, features, idf, vocabulary, length_corpus, chunks_corpus_raw, title_corpus_raw, learning_factor = load_data('corpus_data')
    
    query = [query]
    query = construct_corpus(query)
    query = query[0].split()
    
    
    total_term = 0
    tf = {}
    for x in query:
        if x in vocabulary:
            tf[x] = tf.setdefault(x , 0) + 1
            total_term += 1
    for x in tf:
        tf[x] = tf[x]/total_term
        
    tfidf = {}
    for x in tf:
        tfidf[x] = tf[x] * idf[vocabulary[x]]
    need_sqrt = 0
    for x in tfidf:
        need_sqrt += tfidf[x] * tfidf[x]
        
    sqrt = math.sqrt(need_sqrt)
    for x in tfidf:
        tfidf[x] = tfidf[x] / sqrt
        
    store = [tfidf]
    store = np.array(store)
    np.save('query_data.npy',store)
    
    dic_rank = {}
    for j in range(len(corpus_sorted)):
        chunk = corpus_sorted[j]
        query_tfidf = []
        chunk_tfidf = []
        theta = []
        for term in tfidf:
            if term in chunk:
                query_tfidf.append(tfidf[term])
                chunk_tfidf.append(chunk[term])
                theta.append(learning_factor[j][term])
        #sqrt = math.sqrt(sum(x*x for x in query_tfidf)) * math.sqrt(sum(y*y for y in chunk_tfidf))
        sum_multi = 0
        for i in range(len(query_tfidf)):
            sum_multi += query_tfidf[i] * chunk_tfidf[i] * theta[i]
    #    if sqrt != 0:
    #        chunk_query_score = sum_multi / sqrt
    #    else:
    #        chunk_query_score = 0
            
        dic_rank[j] = sum_multi
        
        
    sorted_rank = sorted(dic_rank.items(), key = lambda x : x[1], reverse=True)
    if sorted_rank[0][1] < 0.05:
        return 'Sorry, we cannot find anything about your query. Do you have another question?'
    #result = [sorted_rank[0][0] + 1,sorted_rank[1][0] + 1,sorted_rank[2][0] + 1,sorted_rank[3][0] + 1]
    #result = [sorted_rank[0][0] + 1,sorted_rank[1][0] + 1,sorted_rank[2][0] + 1,sorted_rank[3][0] + 1, sorted_rank[4][0] + 1,sorted_rank[5][0] + 1,sorted_rank[6][0] + 1,sorted_rank[7][0] + 1,sorted_rank[8][0] + 1,sorted_rank[9][0] + 1]
    #print([sorted_rank[0][1],sorted_rank[1][1] ,sorted_rank[2][1] ,sorted_rank[3][1], sorted_rank[4][1],sorted_rank[5][1],sorted_rank[6][1] ,sorted_rank[7][1] ,sorted_rank[8][1],sorted_rank[9][1]])
    max_answer = 4
    result = [sorted_rank[i][0] + 1 for i in range(max_answer)]
#        
#    for x in result:
#        b = x - 736
#        print(str(x) + '\t'+str(b))
    
    for i in range(len(result)):
        if result[i] > length_corpus:
            result[i] -= length_corpus

        
    new_result = []
    for x in result:
        if x not in new_result:
            new_result.append(x)
    result = new_result
    answer_list = []
    for x in result:
        one_answer = title_corpus_raw[x-1] + ': ' + chunks_corpus_raw[x-1]
        answer_list.append(one_answer)
#        
#    for x in result:
#        print(x)
    #print(length_corpus)
    
    
        
    result_index = {}
    for i in range(len(result)):
        result_index[i+1] = result[i] - 1 + length_corpus
        
    
    result_index = [result_index]
    result_index = np.array(result_index)
    np.save('result_index.npy',result_index)
        
        
        
    
    
    
#    answer1 = title_corpus_raw[result[0]-1] + '\t' + chunks_corpus_raw[result[0]-1]
#    answer2 = title_corpus_raw[result[1]-1] + '\t' + chunks_corpus_raw[result[1]-1]
#    answer3 = title_corpus_raw[result[2]-1] + '\t' + chunks_corpus_raw[result[2]-1]
#    answer4 = title_corpus_raw[result[3]-1] + '\t' + chunks_corpus_raw[result[3]-1]
#    
    answer = ''
    for i in range(len(answer_list)):
        answer = answer + 'Suggested Answer' + str(i+1) + ':\n' + answer_list[i] + '\n\n'
#    for x in answer_list:
#        answer = answer + 'Suggested Answer:\n' + answer1 + '\n\n'
#    answer =  'Suggested Answer1:\n' + answer1 + '\n\n' + \
#            'Suggested Answer2:\n' + answer2 + '\n\n' +\
#            'Suggested Answer3:\n' + answer3 + '\n\n' +\
#            'Suggested Answer4:\n' + answer4
    answer = answer + 'If one of suggested answers you think is the best, could you please give me a short feedback?\n'
            
    return answer



                



    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    

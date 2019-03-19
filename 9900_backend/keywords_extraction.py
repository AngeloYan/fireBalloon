#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 23:36:46 2019

@author: hal
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import construct_corpus


def keywords_extracted_tfidf():

    chunks_corpus_raw = []
    with open('answer_content.txt') as f:
        for line in f:
            chunks_corpus_raw.append(line.splitlines()[0])
    
    chunks_corpus = construct_corpus(chunks_corpus_raw)
    
    title_corpus_raw = []
    with open('title_content.txt') as f:
        for line in f:
            title_corpus_raw.append(line.splitlines()[0])
    
    titles_corpus = construct_corpus(title_corpus_raw)
    
    chunks_titles_corpus = []
    for i in range(len(chunks_corpus)):
        chunks_titles_corpus.append(chunks_corpus[i] + 2 * (' ' + titles_corpus[i]))
        
        
    questions_corpus_raw = []
    with open('question_content.txt') as f:
        for line in f:
            questions_corpus_raw.append(line.splitlines()[0])
    
    questions_corpus = construct_corpus(questions_corpus_raw)
    
    
    
    corpus = questions_corpus + chunks_titles_corpus
    
    
    vectorizer = TfidfVectorizer(smooth_idf = False)
    corpus_matrix = vectorizer.fit_transform(corpus)
    corpus_matrix = corpus_matrix.toarray()
    
    features = vectorizer.get_feature_names()
    idf = vectorizer.idf_
    vocabulary = vectorizer.vocabulary_
    len_features = len(features)
    corpus_sorted = []
    for one_corpus in corpus_matrix:
        dic_corpus = {}
        for i in range(len_features):
            #if one_chunk[i] != 0.0:
            if one_corpus[i] > 0.15:
                dic_corpus[features[i]] = one_corpus[i]
            #if len(dic_chunk) > 7:
                #break
        sorted_dic_corpus = dict(sorted(dic_corpus.items(), key = lambda x : x[1], reverse=True))
        corpus_sorted.append(sorted_dic_corpus)
    
    
    return corpus_sorted, features, idf, vocabulary
        
        
            
    #vectorizer = TfidfVectorizer(smooth_idf = False)
    #chunks_titles_matrix = vectorizer.fit_transform(chunks_titles_corpus)
    #chunks_titles_matrix = chunks_titles_matrix.toarray()
    #
    #features = vectorizer.get_feature_names()
    #len_features = len(features)
    #chunks_titles_sorted = []
    #for one_chunk_title in chunks_titles_matrix:
    #    dic_chunk_title = {}
    #    for i in range(len_features):
    #        #if one_chunk[i] != 0.0:
    #        if one_chunk_title[i] > 0.15:
    #            dic_chunk_title[features[i]] = one_chunk_title[i]
    #        #if len(dic_chunk) > 7:
    #            #break
    #    sorted_dic_chunk_title = dict(sorted(dic_chunk_title.items(), key = lambda x : x[1], reverse=True))
    #    chunks_titles_sorted.append(sorted_dic_chunk_title)
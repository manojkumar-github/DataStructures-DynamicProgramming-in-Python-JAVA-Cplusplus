#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

TF-IDF:
class sklearn.feature_extraction.text.TfidfVectorizer(input='content',
encoding='utf-8', decode_error='strict', strip_accents=None, lowercase=True,
 preprocessor=None, tokenizer=None, analyzer='word', stop_words=None,
 token_pattern='(?u)\b\w\w+\b', ngram_range=(1, 1), max_df=1.0, min_df=1,
 max_features=None, vocabulary=None, binary=False,
 dtype=<class 'numpy.float64'>, norm='l2', use_idf=True,
 smooth_idf=True, sublinear_tf=False

CountVectorizer:

class sklearn.feature_extraction.text.CountVectorizer(input='content',
encoding='utf-8', decode_error='strict', strip_accents=None, lowercase=True,
 preprocessor=None, tokenizer=None, stop_words=None,
 token_pattern='(?u)\b\w\w+\b', ngram_range=(1, 1), analyzer='word',
  max_df=1.0, min_df=1, max_features=None, vocabulary=None,
binary=False, dtype=<class 'numpy.int64'>)[source]

TF-IDF vs CountVectorizer:

CountVectorizer is the count of frequency of each word in a document.

TF-IDF:
    - weight is a statistical measure used to evaluate how important a word
    is to a document in a collection or corpus.
    - Implementation: https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089
    - Explained = http://www.tfidf.com/
        TF(Term Frequnect) = (Number of times term t appears in a document)/
                            (Total number of terms in the document)
        IDF(Inverse Document Frequency) = log_e(Total number of documents/
                                        Number of documents with term t in it)
"""
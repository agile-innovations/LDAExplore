#!/usr/bin/python
__author__ = 'Ashwin'
__email__ = 'gashwin1@umbc.edu'

"""
CMSC 691 - Final Project
Visualizing Topics using LDA

AUTHOR: Ashwinkumar Ganesan.
        Kiante Branley

Latent Dirichlet Allocation is a topic modelling method that calculates
the joint probabilities of words across documents and generates the
two distributions:
1. The distribution of topics for each document.
2. The distribution of words for each topic.

This project tries to visualize the topics, the documents and the clusters
that are generated.
"""

from processdata import fileops
from processdata.lda import LDAVisualModel

if __name__ == "__main__":
    word_corpus = fileops.read_dir('20_newsgroups/alt.atheism/')
    lda = LDAVisualModel([word_corpus])
    lda.create_word_corpus([word_corpus])
    lda.train_lda(20)
    topics = lda.get_lda_corpus()

    print topics


__author__ = 'Ashwin'
__email__ = 'gashwin1@umbc.edu'

"""
Basic LDA module that is used in the project.
"""
import re
from gensim import corpora, models


class LDAVisualModel:
    def __init__(self, word_corpus):
        """
        The LDAVisualModel requires list of word lists from the
        document corpus. Each list of words represents a document.
        :param word_corpus: [[<words>],[],[]]
        """
        self.id2word = corpora.Dictionary(word_corpus)
        self.mm = []
        self.lda = None

    def create_word_corpus(self, word_corpus, store_corpus=False, store_loc='dicts/corpus.mm'):
        """
        :param word_corpus: word_corpus: [[<words>],[],[]]
        :param store_corpus: boolean to store the serialized corpus or not.
        :param store_loc: Defines the location where the file is to be stored.
        """
        for text in word_corpus:
            self.mm.append(self.id2word.doc2bow(text))

        if store_corpus:
            corpora.MmCorpus.serialize(store_loc, word_corpus)

    def train_lda(self, num_top=2, update_t=1, chunks=10000, num_pass=1):
        """
        :param num_top: The number of topics for which LDA trains.
        :param update_t:
        :param chunks:
        :param num_pass: The number of passes that LDA executes on the data.
        """
        self.lda = models.LdaModel(corpus=self.mm, id2word=self.id2word, num_topics=num_top,
                                   update_every=update_t, chunksize=chunks, passes=num_pass)

    def get_lda_corpus(self, num_of_topics=10, num_of_words=10):
        """
        Get the topic associated with each document.
        """
        topics = []
        if self.lda:
            for topic in self.lda.print_topics(num_of_topics, num_of_words):
                regex = re.findall(r'(0\.[0-9]*)\*([0-9a-z]*)', topic, re.M | re.I)
                topics.append(regex)

        return topics

    def generate_doc_topic(self):
        # Find the number of topics.
        num_topics = self.lda.num_topics

        print num_topics

        # Build the topic - document matrix.
        doc_top = []
        for idx, doc in enumerate(self.lda[self.mm]):
            doc_top.append([0] * num_topics)
            for topic in doc:
                doc_top[idx][topic[0]] = topic[1]

        return doc_top

    #def gen_doc_top_words(self, topics, doc_top):
        #
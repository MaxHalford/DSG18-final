# https://www.kaggle.com/classtag/cat2vec-powerful-feature-for-categorical
import pandas as pd
import numpy as np
import gc, copy
from gensim.models import Word2Vec # categorical feature to vectors
from random import shuffle
import warnings
warnings.filterwarnings('ignore')


class Cat2Vec:
    def __init__(self,data,cat_cols):
        self.data = data
        self.cat_cols = cat_cols
    
    def apply_w2v(self,sentences):
        def _average_word_vectors(words, model, vocabulary, num_features):
            feature_vector = np.zeros((num_features,), dtype="float64")
            n_words = 0.
            for word in words:
                if word in vocabulary: 
                    n_words = n_words + 1.
                    feature_vector = np.add(feature_vector, model[word])

            if n_words:
                feature_vector = np.divide(feature_vector, n_words)
            return feature_vector
        
        vocab = set(self.model.wv.index2word)
        feats = [_average_word_vectors(s,self.model,vocab,self.n_cat2vec_feature) for s in sentences]
        return np.array(feats)

    def gen_cat2vec_sentences(self):
        X_w2v = copy.deepcopy(self.data.loc[:,self.cat_cols])
        names = list(X_w2v.columns.values)
        for c in names:
            X_w2v[c] = X_w2v[c].fillna('unknow').astype('category')
            X_w2v[c].cat.categories = ["%s %s" % (c,g) for g in X_w2v[c].cat.categories]
        X_w2v = X_w2v.values.tolist()
        return X_w2v
    
    def fit(self,n_cat2vec_feature = None,n_cat2vec_window = None):
        if n_cat2vec_feature is None:
            n_cat2vec_feature  = len(self.cat_cols) # define the cat2vecs dimentions
        if  n_cat2vec_window is None:   
            n_cat2vec_window   = len(self.cat_cols) * 2 # define the w2v window size
        self.n_cat2vec_feature = n_cat2vec_feature
        self.n_cat2vec_window = n_cat2vec_window
        X_w2v = self.gen_cat2vec_sentences()
        for i in X_w2v:
            shuffle(i)
        model = Word2Vec(X_w2v, size=n_cat2vec_feature, window=n_cat2vec_window)
        self.model = model

    def transform(self):
        c2v_matrix = self.apply_w2v(self.gen_cat2vec_sentences())
        self.cat2vec = c2v_matrix
        self.cat2vec = pd.DataFrame(self.cat2vec)
        self.cat2vec = self.cat2vec.add_prefix('cat2vec_')
        return self.cat2vec 
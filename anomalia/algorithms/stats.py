import pandas as pd
import scipy.spatial.distance as dist

#Statistics methods for anomaly detection


def mean(items, eps):
    return pd.Series([item for item in items]).mean() >= eps

def median(items, eps):
    return pd.Series(items).median() >= eps

def qtest(items, value):
    '''
    Q test, is used for identification and rejection of outliers.
    https://en.wikipedia.org/wiki/Dixon's_Q_test
    items is list of Item
    '''
    series = pd.Series(items)
    maxvalue = series.max()
    minvalue = series.min()
    q = (value - minvalue)/(maxvalue - minvalue)


def distance(itemset1, itemset2, eps, method='l2'):
    '''
       Distance between two series
    '''

    func = dist.euclidean
    if method == 'chebyshev':
        func = dist.chebyshev
    if method == 'hamming':
        func = dist.hamming

    return func(itemset1, itemset2) > eps


def correlation(itemset1, itemset2):
    return dist.correlation(itemset1, itemset2)


def gribbs(self, items):
    '''
       Gribbs score
       https://en.wikipedia.org/wiki/Grubbs'_test_for_outliers
    '''
    series = pd.Series(items)
    mean = series.mean()
    std = series.std()
    size = series.size()
    z_score = (items - mean) / std



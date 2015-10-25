from sklearn import preprocessing
from scipy import ndimage


class Preprocessing:
    def __init__(self, data):
        self._data = data

    def scale(self):
        ''' Standardization of data
        '''
        return preprocessing.scale(self._data)

    def normalize(self):
        ''' Normalization of data
        '''
        return preprocessing.normalize(self._data, norm='l2')

    def img_preprocess(self):
        return ndimage.gaussian_filter(self._data, 5)


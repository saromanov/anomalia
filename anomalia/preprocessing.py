from sklearn import preprocessing
from scipy import ndimage, misc


class Preprocessing:
    def __init__(self, data):
        self._data = data

    def scale(self):
        return preprocessing.scale(self._data)

    def normalize(self):
        return preprocessing.normalize(self._data, norm='l2')

    def img_preprocess(self):
        return ndimage.gaussian_filter(img, 5)


from scipy import ndimage


def img_preprocess(self):
    return ndimage.gaussian_filter(self._data, 5)


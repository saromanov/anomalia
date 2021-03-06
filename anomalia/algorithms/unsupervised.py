from sklearn.clustering import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

#Anomaly detection with unsupervised learning algorithms

class Unsupervised:
    def __init__(self, data):
        self._data = data

    def kmeans(self, items, clusters=3):
        ''' KMeans algorithms for clustering data
        '''
        model = KMeans(n_clusters=clusters, init='k-means++')
        model.fit(items)
        return model.predict(items)

    def pca(self, items, components=3):
        ''' Principal component analysis for dimension reduction
            and data decomposition
        '''
        pca = PCA(n_components=components)
        return pca.fit(X)

    def tsne(self, items, components=3):
        '''
           t-SNE algorithm for manifold learning
        '''
        model = TSNE(n_components=components, init='pca')
        return model.fit_transform(items)



from sklearn.linear_model import LogisticRegression
from sklearn import svm

#Supervised learning algorithms for failure detection

class Suprevised:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def logistic(self, pred):
        model = LogisticRegression(penalty='l1', tol=0.01)
        model.fit(self.data, self.labels)
        return model.predict(pred)

    def svm(self, pred):
        model = svm.SVC()
        model.fit(self.data, self.labels)
        return model.predict(pred)


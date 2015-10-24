from sklearn.linear_model import LogisticRegression

#Supervised learning algorithms for failure detection

class Suprevised:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def logistic(self, pred):
        model = LogisticRegression(penalty='l1', tol=0.01)
        model.fit(self.data, self.labels)
        return model.predict(pred)


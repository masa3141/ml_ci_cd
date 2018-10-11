from base import BaseEstimator

class W2V(BaseEstimator):
    def printa(self):
        print("a")

    def fit(self):
        print('fit')

    def predict(self):
        print('predict')

a = W2V()
a.printa()

a
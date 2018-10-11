from base import BaseEstimator


class D2V(BaseEstimator):
    def __init__(self, train_data, test_data):
        super(D2V, self).__init__(train_data, test_data)

    def print_d2v(self):
        print("a")

    def fit(self):
        print(self.train_data)
        print('d2v fit')

    def predict(self):
        print('d2v predict')
        print(self.test_data)
        return [i*i for i in self.test_data]

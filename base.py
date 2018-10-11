from abc import ABCMeta, abstractmethod
class BaseEstimator(metaclass=ABCMeta):
    """Base class for all estimators in scikit-learn

    Notes
    -----
    All estimators should specify all the parameters that can be set
    at the class level in their ``__init__`` as explicit keyword
    arguments (no ``*args`` or ``**kwargs``).
    """
    def __init__(self, train_data, test_data):
        self.train_data = train_data
        self.test_data = test_data

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

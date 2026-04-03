from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.metaestimators import available_if

class ClassifierWithLabelEncoderMixin:
    

    def fit(self,X,y):
        return super().fit(X,y)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def show_feature_importances(title: str, dataframe: pd.DataFrame, model):
    n_features = dataframe.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), dataframe.columns)
    plt.xlabel('Feature Importance')
    plt.ylabel('Feature')
    plt.title(title)


def score_model(model, train_data, train_labels, test_data, test_labels):
    print("Accuracy on training set: {:.3f}".format(model.score(train_data, train_labels)))
    print("Accuracy on test set: {:.3f}".format(model.score(test_data, test_labels)))

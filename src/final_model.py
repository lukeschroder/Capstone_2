from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import sys

def evaluate(X_train,y_train,X_test):
    model = GradientBoostingRegressor(learning_rate=0.2,max_depth=9,min_samples_leaf=15
                                        ,max_features='auto',n_estimators=150,max_leaf_nodes=8)
    
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    RMSE = mean_squared_error(y_test,y_pred,squared=False)

    return RMSE

if __name__ == '__main__':
    y_train = pd.read_csv('../data/y_train.csv',index_col='Unnamed: 0')
    y_train = y_train['0']
    X_train = pd.read_csv('../data/X_train.csv',index_col='Unnamed: 0')

    y_test = pd.read_csv('../data/y_test.csv',index_col='Unnamed: 0')
    y_test = y_test['0']
    X_test = pd.read_csv('../data/X_test.csv',index_col='Unnamed: 0')

    RMSE = evaluate(X_train,y_train,X_test)

    print(RMSE)

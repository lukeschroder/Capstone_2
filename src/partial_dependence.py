from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.inspection import partial_dependence, plot_partial_dependence
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



if __name__ == '__main__':
    y_train = pd.read_csv('../data/y_train.csv',index_col='Unnamed: 0')
    y_train = y_train['0']
    X_train = pd.read_csv('../data/X_train.csv',index_col='Unnamed: 0')

    y_test = pd.read_csv('../data/y_test.csv',index_col='Unnamed: 0')
    y_test = y_test['0']
    X_test = pd.read_csv('../data/X_test.csv',index_col='Unnamed: 0')

    model = GradientBoostingRegressor(learning_rate=0.2,max_depth=9,min_samples_leaf=15
                                        ,max_features='auto',n_estimators=150,max_leaf_nodes=8)
    
    model.fit(X_train,y_train)

    print(X_train.columns)
    fig, ax = plt.subplots(figsize=(18,18))
    my_plots = plot_partial_dependence(model,       
                                   features=[15,16,17,18,19,20,21,22,23,24,25], # column numbers of plots we want to show
                                   X=X_train,            # raw predictors data.
                                   feature_names=list(X_train.columns), # labels on graphs
                                   grid_resolution=100,
                                   percentiles=(.01,.99),
                                   ax=ax) # number of values to plot on x axis

    plt.show()
    # plt.savefig('../images/partial_dependence_nuke.png',dpi=60)
    
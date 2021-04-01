import pandas as pd
import numpy as np

def train_test_split(df):
    
    test = df[df['DATAYEAR'] >= 2018]
    train = df[df['DATAYEAR'] < 2018]
    
    return train, test

def X_y_split(df):
    y = pd.Series(df['TOTALREVENUE']/df['TOTALSALES'])
    ab = np.abs(y.min())
    y = np.log(y+ab+.000000001)
    X = df.drop(columns=['TOTALREVENUE','TOTALSALES']).copy()
    return X, y

if __name__ == '__main__':
    sixty = pd.read_csv('../data/combined_cleaned.csv',dtype={'WINTERPEAKDEMAND': np.float64, 'SUMMERPEAKDEMAND': np.float64},index_col='Unnamed: 0')

    sixty['TOTALSALES'] = sixty['TOTALSALES'].replace(to_replace=0, value=1)
    sixty['TOTALREVENUE'] = sixty['TOTALREVENUE'].replace(to_replace=0, value=1)

    sixty = sixty.drop(columns=['UTILITYCODE','UTILITYNAME'])

    sixty = sixty.dropna()

    train, test = train_test_split(sixty)

    X_train, y_train = X_y_split(train)
    X_test, y_test = X_y_split(test)
    train.to_csv('../data/eda.csv')
    X_train.to_csv('../data/X_train.csv')
    y_train.to_csv('../data/y_train.csv')
    X_test.to_csv('../data/X_test.csv')
    y_test.to_csv('../data/y_test.csv')

    print(y_train.max()-y_train.min())
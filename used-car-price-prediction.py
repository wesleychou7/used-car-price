import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing
from scipy.stats import norm
from myutils import remove_nonnumeric

# URL for database
url = "data/cars-dataset1.csv"

def clean_data(url):
    
    df = pd.read_csv(url)
    
    # initialize features for filtered dataset
    new_df = {}
    names = ['name', 'year', 'mileage', 'used/cert', 'price']

    for name in names:
        new_df[name] = []
        
    # filter data and put into new data file (new_df)
    for sample in df.values:
        
        # Ignore rows that have Mileage = 'Mileage' or Price = 'Not Priced'
        if sample[1] == 'Mileage' or sample[5] == 'Not Priced':
            continue
        
        new_df['name'].append(sample[0][5:].lower())
        new_df['year'].append(int(sample[0][0:4]))
        new_df['mileage'].append(int(remove_nonnumeric(sample[1])))

        # used -> 0 ; certified -> 1
        if sample[4] == 'Used':
            new_df['used/cert'].append(0)
        else:
            new_df['used/cert'].append(1)

        new_df['price'].append(int(remove_nonnumeric(sample[5][:-3])))

    df = pd.DataFrame(new_df)
    df.to_csv()
    
    return df


def get_subdata(df, make, model, trim):

    # Get sub-dataset of that car (all cars with the same name)
    user_input = " ".join([make, model, trim]).lower()
    count = 0

    X_train = np.empty((0,3)) # empty 2D array with 0 rows, 3 columns
    y_train = np.array([])    # empty 1D array with 0 elements

    for sample in df.values:
        if user_input in sample[0]:
            X_train = np.vstack((X_train, sample[1:4]))
            y_train = np.append(y_train, sample[4])
            
    return X_train, y_train 


def scale_data(X):
    
    scaler = preprocessing.RobustScaler()
    scaled_X = scaler.fit_transform(X)
    
    return scaled_X


def create_model(scaled_X_train, y_train):
    
    # create a multivariate linear regression model
    model = linear_model.LinearRegression()
    model.fit(scaled_X_train, y_train)
    
    return model

    
def predict_price(make, model, trim, year, mileage, usedcert):
    """
    combine everything
    """
    # clean data
    df = clean_data(url)
    # get subdata
    X, y = get_subdata(df, make, model, trim)
    # scale subdata
    X_scaled = scale_data(X)
    
    # create linear regression model
    ML_model = create_model(X_scaled, y)
    # scale input
    scaled_in = scale_data([[year, mileage, usedcert]])
    # predict price
    price = ML_model.predict(scaled_in)
    
    # return price, rounded to nearest dollar
    return round(price[0])



def main():
    
    make, model, trim = None, None, None         # these should be strings
    year, mileage, usedcert = None, None, None   # these should be integers
    
    # get user input
    make = input("Enter make: ")
    model = input("Enter model: ")
    trim = input("Enter trim: ")
    year = input("Enter year: ")
    mileage = input("Enter mileage: ")
    print("Is your car used or certified? ")
    usedcert = input("Enter 0 for used, 1 for certified: ")
    
    # predict price and print it
    price = predict_price(make, model, trim, year, mileage, usedcert)
    print(f"Predicted price: ${price}")

if __name__ == "__main__":
    main()
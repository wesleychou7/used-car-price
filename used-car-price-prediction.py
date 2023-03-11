import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing
from scipy.stats import norm
from myutils import remove_nonnumeric

# URL for database
url = "data/cars-dataset1.csv"

def predict_price(make, model, trim, year, mileage):
    
    
    
    return None



def main():
    
    make, model, trim = None, None, None  # these should be strings
    year, mileage = None, None            # these should be integers
    
    # get input
    
    # output predicted price
    price = predict_price(make, model, trim, year, mileage)
    print(f"Predicted price: ${price}")

if __name__ == "__main__":
    main()
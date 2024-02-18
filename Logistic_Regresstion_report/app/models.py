from django.db import models

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('app/templates/data.csv')

regression = LinearRegression()

trained = pd.DataFrame({'Bedrooms':data['bedrooms'],
                        'Bathrooms':data['bathrooms'],
                        'Floors':data['floors'],
                        'Sqft_Living':data['sqft_living']
                       })

Prd_Value = data['price']




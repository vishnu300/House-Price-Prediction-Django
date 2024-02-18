from django.shortcuts import render

from .models import trained,train_test_split ,regression ,Prd_Value
from django.db import models
from sklearn.model_selection import train_test_split
import xgboost

from xgboost import XGBRegressor

def home(reque):
    return render(reque ,'housePrice.html')

x_train,x_test,Prdi_trained, Prdi_test = train_test_split(trained,Prd_Value ,test_size = 30)

regression.fit(x_test,Prdi_test)

xgb= XGBRegressor()

xgb.fit(x_test,Prdi_test)

# views.py
from django.shortcuts import render

def price(request):
    var1 =float(request.GET['v1'])
    var2 =float(request.GET['v2'])
    var3 =float(request.GET['v3'])
    var4 =float(request.GET['v4'])
    
    y_pred = xgb.predict([[var1,var2,var3,var4]])

    return render (request,'housePrice.html', {'result1': y_pred})

   
   

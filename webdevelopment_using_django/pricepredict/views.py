from django.shortcuts import render
import pickle
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
# Create your views here.
def home(request):
    if request.method == 'POST':
        bikesval = request.POST.get('bikeslist')
        with open(f'webdevelopment_using_django/pricepredict/hamrobazar models/{bikesval}', 'rb') as f:
            model = pickle.load(f)
        lotnoval = request.POST.get('lotno')
        kilometersval = request.POST.get('kilometers')

        # print(lotnoval)
        # print(kilometersval)
        # print(bikesval)

        pf = PolynomialFeatures(2, interaction_only=False)
        x = pf.fit_transform([[int(lotnoval), int(kilometersval)]])
        y = model.predict(x)

        # print(y[0])
        a = np.round(y[0])

        # Arranging the final price by adding ,
        a = str(int(a))
        a = list(a)
        i = -3
        while a[2] != ',' and a[1] != ',':
            a.insert(i, ',')
            i = i - 3
        a = ''.join(a)
        context = {'Result': a}

        return render(request, 'pricepredict/home.html', context)

    else:
        return render(request, 'pricepredict/home.html')


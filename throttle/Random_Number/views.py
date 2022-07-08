from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

ramdom_list=['^j&i 1','abc','xyz','pqr','lmn']
def random_number(request):
    rand_num1 = random.randint(1000,9999)
    print("------------------------", rand_num1)

    rand_num2 = random.random()
    print("------------------------", rand_num2)

    rand_range = random.randrange(0,599)
    print("------------------------", rand_range)

    # print("------------------------", {{ ramdom_list|random }} )
    return HttpResponse("Random Number .....")
from django.http import JsonResponse
from bson.json_util import dumps,loads
import pymongo
import json
import pandas as pd
from bson import json_util
from bson import ObjectId

from django.shortcuts import render
def dashboard(request):
    return render(request,"datavisulize.html")
def dashboard1(request):
    return render(request,"newfile.html")
def fetchitem(request):
    try:
         client = pymongo.MongoClient("mongodb://localhost:27017/")
         db = client["data"]
         collection = db['dataitems']
         p=collection.find()

         user=[]
         for i in p:
             user.append(i)

         return JsonResponse(dumps(user), safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'data': []}, safe=False)
def year(request):
    try:
        e = request.GET['endyear']
        y=int(e)
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["data"]
        collection = db['dataitems']
        t = collection.find({'end_year':y})

        return JsonResponse(dumps(t), safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'data': []}, safe=False)
def countryyear(request):
    try:
        e = request.GET['endyear']
        c = request.GET['country']
        y=int(e)
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["data"]
        collection = db['dataitems']
        t = collection.find({'end_year':y,'country':c})

        return JsonResponse(dumps(t), safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'data': []}, safe=False)

def country(request):
        try:
            c = request.GET['country']
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["data"]
            collection = db['dataitems']
            t = collection.find({'country': c})

            return JsonResponse(dumps(t), safe=False)
        except Exception as e:
         print(e)
        return JsonResponse({'data': []}, safe=False)

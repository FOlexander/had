from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# from .kmcox import createDashboard
from django.http import HttpResponse
from . import survivalcalc
import time
from .models import Plot
import pandas as pd
import numpy as np
import pyexcel

#в этот файл подключаем файл аналитики. Внутри индекса передаем данные

# Create your views here.
def index(request):
        return render(request, 'main/index.html')

def datadownload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        # wb = openpyxl.load_workbook(uploaded_file)
        # ws = wb.active
        # df = pd.DataFrame(ws.values)
        print(uploaded_file.name)
        sheet = pyexcel.get_sheet(file_name=f'media/{uploaded_file.name}')
        a = []
        for i in sheet:
            a.append(i)
        my_array = np.array(a)
        df = pd.DataFrame(my_array)

        new_header = df.iloc[0]  # grab the first row for the header
        df = df[1:]  # take the data less the header row
        df.columns = new_header  # set the header row as the df header

        filename = uploaded_file.name
        if filename.split(".")[-1] == "xlsx":
            filename = filename.replace("xlsx", "png")
        elif filename.split(".")[-1] == "csv":
            filename = filename.replace("csv", "png")
        elif filename.split(".")[-1]  == "xls":
            filename = filename.replace("xls", "png")
        # uploaded_file_url = fs.url(filename)
        # createDashboard(uploaded_file.name)
        v = survivalcalc.dataStructure(df,filename)
        time.sleep(1.4)#нужно дорисовать сюда красивую загрузку
        plot = Plot.objects.all()
        return render(request, 'main/chart.html', v)
    return render(request, 'main/datapreparation.html')
#
# def mun(request):
#     return HttpResponse("<h1>Mun page for <a href='/ruf'>everybody</a></h1>")
#
# def ruf(request):
#     return HttpResponse("<h1>Первый <a href='/about'>заоголовок</a></h1> <h2>Второй заоголовок</h2> <br\> <h3>Третий заоголовок</h3>")

# def upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         print(uploaded_file.name)
#         print(uploaded_file.size)
#     return render(request, 'main/simple_upload.html')

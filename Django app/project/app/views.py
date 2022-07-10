from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
import csv
from django.utils.encoding import smart_str

# download the data to a csv file
def download_csv_data(request):
   # response content type
   response = HttpResponse(content_type='text/csv')

   #decide the file name
   response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.csv"'

   writer = csv.writer(response, csv.excel)
   response.write(u'\ufeff'.encode('utf8'))

   #write the headers
   writer.writerow([
     smart_str(u"Project Name"),
     smart_str(u"Project Description"),
     smart_str(u"Start Date"),
     smart_str(u"End Date"),
     smart_str(u"Duration"),
   ])

   #get data from database or from text file....
   projects = Project.objects.all() 
   for event in projects:
     writer.writerow([
        smart_str(event.name),
        smart_str(event.description),
        smart_str(event.start_date),
        smart_str(event.end_date),
        smart_str(event.duration),
     ])
   return response

# Create your views here.
# just a home page
def home(request):
    return HttpResponse('Hey There!')


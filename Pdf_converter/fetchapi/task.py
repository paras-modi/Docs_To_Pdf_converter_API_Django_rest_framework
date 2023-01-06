

import os
from celery import shared_task
import celery
from django.core.files.storage import FileSystemStorage
from docx2pdf import convert




@shared_task()
def convert_to_pdf(file):
  
    # Simulate expensive operation(s) that freeze Django
    try:

      #fs = FileSystemStorage()
      #print('hi')
      #print(file.name)
      #print(celery.current_task.tasl_id)
     # filename=fs.save(file.name,file)
      #file.name= self.request.id
    #rint(self.task_id)
      #print(STATIC_ROOt)
      #file= STATIC_ROOt + '/' +file
      
      #name= self.request.id
      #print(name)
     
      convert(file)
      #os.delete(dest)
      #fs = FileSystemStorage()
      #uploaded_file_url=fs.url(name +'.docx')
      

    except Exception as e:
        print(e)



    return None 



@shared_task()
def pdf():
  
    # Simulate expensive operation(s) that freeze Django
    try:

      print("hello")
    except Exception as e:
        print(e)



    return None
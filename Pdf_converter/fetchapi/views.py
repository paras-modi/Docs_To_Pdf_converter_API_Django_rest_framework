# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser



from celery.result import AsyncResult
from Pdf_converter.settings import STATIC_DIR, STATIC_ROOt

from fetchapi.task import  convert_to_pdf

def home(request):

    return render(request, 'home.html' )


class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
           
            #print(request.data['files'][0])
            File=request.FILES['files']
            fs = FileSystemStorage()
            filename=fs.save(File.name,File)
            #print(filename)
            name= STATIC_ROOt + '/'+ filename
            x=convert_to_pdf.delay(name)
            list=filename.rsplit('.',1)
            # print(list[0])
            
            print("working")
            
            return Response({
                    'status': 201,
                    'message': 'files uploaded successfully',
                    'id': x.task_id,
                    'name': list[0]


                      })

            
        except Exception as e:
            print(e)
            return Response({
                'status': 400,
                'message': 'somethign went wrong',
                'id': 'not found',

                 })

    def get(self,request,task_id):
        try:
            res=AsyncResult(task_id)
            if res.ready():
                return Response({
                    'status':401,
                    'message':'sucessfull',
                })
            else:
                return Response({
                    'status': 402,
                    'message': 'unsucessfull',
                })

        except Exception as e:
            print(e)



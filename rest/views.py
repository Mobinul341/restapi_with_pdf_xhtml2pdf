from django.shortcuts import render
from django.template.loader import get_template
from .models import PostModel
from .serializers import PostModelSerializers
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views import View
from django.views.generic import ListView
from .utils import render_to_pdf

#Class base view
#1. Basic CBV 
class FirstView(View):
    template_name = 'classic_1.html'
    context={"greet":"Hello basic CBV"}
    def get(self, request):
        
        return render(request, self.template_name, self.context)

#2 Basic inheritance
class FirstInheritView(View):
    template_name = 'classic_1.html'
    context = {"greet":"Hello basic CBV inheritance"}

    def get(self, request):
        return render(request, self.template_name, self.context)

#3. Basic Generic CBV listview
class PostListView(ListView):
    model = PostModel.objects.all()
    context = {"model":model}
    template_name = 'listview.html'
    def get(self, request):
        return render(request, self.template_name, self.context)
#4. GCBV with pdf rendering & generating
## https://xhtml2pdf.readthedocs.io/en/latest/format_html.html
class GeneratePdfView(View):
    template_name = 'listview.html'
    model = PostModel.objects.all()
    context = {"model":model}

    def get(self, request, *args, **kwargs):
        template = get_template(self.template_name)
        context = self.context

        html = template.render(context)
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type = 'application/pdf') #It can be result simply
        '''
        if pdf:
            response = HttpResponse(pdf, content_type = 'application/pdf')
            filename = "Simple Blog %s.pdf"%("From Kawshik")
            content = "inline; filename='%s'"%(filename)
            download = request.GET.get('download')

            if download:
                content = "attachment; filename='%s'"%(filename)
            response['Content-Disposition'] = content
        return HttpResponse("Not Found")
        '''

















#Function Base view
def index(request):
    return render(request, 'index.html', {"body":"Hello WOrld"})

#1.csrf_exempt is a decorator which ensures protection from the middleware
#2. api_view 
@api_view(['GET', 'POST'])
@csrf_exempt
def posts(request):
    
    if request.method == 'GET':
        posts = PostModel.objects.all()
        serializer = PostModelSerializers(posts, many=True)
        #return JsonResponse(serializer.data, safe=False)
       
        return Response(serializer.data)

    elif request.method == 'POST':
        
        #data = JSONParser().parse(request)
        serializer = PostModelSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def post_list_id(request, post_id):
    try:
        post = PostModel.objects.get(id=post_id)
    except PostModel.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostModelSerializers(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        #data = JSONParser().parse(request)
        serializer = PostModelSerializers(post,data=request.data #data=data)

        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return Response(serializer.data)
        #return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=204)
'''


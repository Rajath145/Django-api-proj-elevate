from django.shortcuts import render
from .models import movies
from movieapp.serializers import MoviesSerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def movieapi(request,id=0):
    if request.method == 'GET':
        movie=movies.objects.all()
        print(movie)
        movies_serializers=MoviesSerializers(movie,many=True)
        return JsonResponse(movies_serializers.data,safe=False)
    elif request.method=='POST':
        moviess=JSONParser().parse(request)
        moviess_serializers=MoviesSerializers(data=moviess)
        if moviess_serializers.is_valid():
            moviess_serializers.save()
            return JsonResponse("data add successfully",safe=False)
        return JsonResponse("not added")
    elif request.method=="PUT":
        movieid=JSONParser().parse(request)
        moviessdata=movies.objects.get(id=movieid['id'])
        movie_serializer=MoviesSerializers(moviessdata,data=movieid)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("It is successfully updated",safe=False)
        return JsonResponse("Not Updated",safe=False)
    elif request.method=="DELETE":
        var1=movies.objects.get(id=id)
        var1.delete()
        return JsonResponse("It is deleted Successfully.....",safe=False)
    return render(request,"index.html")

def index(request):
    serializer=MoviesSerializers
    return render(request,"index.html",{'serializer':serializer})
    


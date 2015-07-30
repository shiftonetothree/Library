from django.shortcuts import render_to_response, RequestContext
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from bookLib.serializers import *
from django.db.models import Q

def template(request):
    return render_to_response('h1.html',context_instance=RequestContext(request))
def template2(request):
    return render_to_response('h1.html',context_instance=RequestContext(request))
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self, request, **kwargs):
        keyword=kwargs.get('keyword')
        if keyword==None or keyword=='':
            b=Book.objects.filter()
        else:
            b = Book.objects.filter(
                Q(title__icontains=keyword)|
                Q(name__icontains=keyword)|
                Q(author__icontains=keyword)|
                Q(time__icontains=keyword)
            )
        ser = BookSerializer(b,many=True)
        return Response(ser.data)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # def get(self, request, pk):
    #     try:
    #         b = Book.objects.get(name=pk)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     ser = BookSerializer(b)
    #     return Response(ser.data)

    # def delete(self, request, pk):
    #     try:
    #         b = Book.objects.get(name=pk)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     b.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def patch(self, request, pk):
    #     try:
    #         b = Book.objects.get(name=pk)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def put(self, request, pk):
    #     try:
    #         b = Book.objects.get(name=pk)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
from django.shortcuts import render,get_object_or_404
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .validation import validate_name_space

# Create your views here.
@api_view(['GET', 'POST'])
def person_list(request):
    if request.method == "GET":
        persons = Person.objects.all()
        name = request.GET.get("name")   # get the query parameter name 
        
        if name:
            name = validate_name_space(name)  #A function created for data validation
            persons = Person.objects.filter(name=name)
        serializer=PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def person_detail(request,pk):
    try:
        person = get_object_or_404(Person,id=pk) #get the person object by id 
    except ValueError:
        name = validate_name_space(pk)
        person = get_object_or_404(Person,name=name) #get the person object by name if a name was passed instead of id
    
    if request.method == 'GET':         
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
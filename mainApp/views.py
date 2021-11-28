from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from . import models
from rest_framework.decorators import api_view



@api_view(['GET'])
def getAllNews(request):
    data =[]
    image =''
    for news in models.News.objects.all():
        try:
            "try if this news has Image In it Just In Case"
            image = news.image.url
        except:
            "this means there is no image so it will just return empty string"
            image =''

        data.append({
            'image':image
            ,
            'id':news.id,'heading':news.heading,
            'intro_content':news.intro_content
        })

    return Response(data={
        'message':"Success",
        "data":data
    },status=status.HTTP_200_OK)



@api_view(['POST'])
def registration_form(request):
    first_name= request.data['first_name']
    last_name= request.data['last_name']
    phone_number= request.data['phone_number']
    email= request.data['email']
    sex= request.data['sex']
    age= request.data['age']
    state= request.data['state']
    local_govt= request.data['local_govt']

    registerationModel = models.RegisterData.objects.create(
        first_name=first_name,
        last_name = last_name,
        phone_number=phone_number,
        email = email,
        sex= sex,
        age=age,
        state = state,
        local_govt=local_govt
        )

    registerationModel.save()

    # 
    return Response("Thank You For Being A Part Of this Movement",status=status.HTTP_200_OK)
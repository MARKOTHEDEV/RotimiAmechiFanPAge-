from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from . import models
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from .customErrorResponses import CustomError
from . import serializer

from rest_framework.authtoken.models import Token

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
    ward= request.data['ward']
    unit= request.data['unit']
    stateOfOrigin = request.data['stateOfOrigin']
    voters_identification_number = request.data['voters_identification_number']

    registerationModel = models.RegisterData.objects.create(
        first_name=first_name,
        last_name = last_name,
        phone_number=phone_number,
        email = email,
        sex= sex,
        age=age,
        state = state,
        local_govt=local_govt,ward=ward,unit=unit,
        stateOfOrigin=stateOfOrigin, voters_identification_number=voters_identification_number
        )

    registerationModel.save()

    # 
    return Response("Thank You For Being A Part Of this Movement",status=status.HTTP_200_OK)




# endpoint to get all blog post
@api_view(['POST'])
def getAllBlogpost(request):
    "this get all the blog Post"
    blog_postsFromDB = models.BlogPosts.objects.all().filter(is_approved=True)
    # this is an  empty list that will contain all the blog post which will be dict
    all_blog_post=[]
    for blog in blog_postsFromDB:
        all_blog_post.append(
            {'id':blog.id,'title':blog.title,
            "author":blog.author.full_name(),
            'main_image':blog.main_image.url,
            "paragraphs":blog.blogcontent_set.all().values('id','text'),
            }
        )
    return Response(data={
        'message':"Success",
        "data":all_blog_post
    },status=status.HTTP_200_OK)
# endpoint to get blogDetail
@api_view(['GET'])
def getBlogDetail(request,blogID):
    if not models.BlogPosts.objects.filter(id=blogID).exists():
        raise CustomError("This Blog Post has been deleted or does't exist")


    blogDetail = models.BlogPosts.objects.get(id=blogID)

    data = {'id':blogDetail.id,'title':blogDetail.title,
            "author":blogDetail.author.full_name(),
            'main_image':blogDetail.main_image.url,
            "paragraphs":blogDetail.blogcontent_set.all().values('id','text'),
            }
    return Response(data={
        'message':"Successfull",
        'data':data
    })

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def creteBlog(request):
    pass




# endpoint to create a blogPost and Update













class UserLogin(ObtainAuthToken):
    "this Helps to Login A Existing User"
    
    serializer_class = serializer.UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                        'token':token.key,
                        "first_name":user.first_name,
                        "last_name":user.first_name,
                    }

            return Response({
                    'message':'Login Successfull',
                    'status_code':status.HTTP_200_OK,
                    'data':data
            })
        raise CustomError("Check Your Credentials!")

class UserRegistrationViewSets(viewsets.ViewSet):
    serializers = serializer.UserRegistrationSerializer
    

    # @action(detail=False, methods=['post'])
    def create(self,request,pk=False):
        serializedData = self.serializers(data=request.data)
        if serializedData.is_valid(raise_exception=True):
            
            user = serializedData.save()
            # i want to give the user a token on the create of the user
            token = Token.objects.create(user=user)
            data = {
                    'token':token.key,
                    "first_name":user.first_name,
                    "last_name":user.last_name,
                    # "user_type":user.user_types
                }

            return Response(data={
                'message':'Successfully Created',
                'status_code':status.HTTP_200_OK,
                'data':data
            },status=status.HTTP_200_OK)

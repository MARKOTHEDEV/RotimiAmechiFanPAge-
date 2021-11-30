
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from mainApp import models
from .customErrorResponses import CustomError



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[],required=False)
    password = serializers.CharField(validators=[],required=False)



    def validate(self, attrs):
        email = attrs.get('email',None)
        password = attrs.get('password',None)

        
        if email is None or len(email) == 0:
            raise CustomError(message=f'Email is required')
        


        if password is None or len(password) == 0:
            raise CustomError(message=f'Password is required')

        if not get_user_model().objects.filter(email=email).exists():
            raise CustomError(message='Email Does Not Exist Please Check Your Spelling')
        else:
            user =get_user_model().objects.get(email=email)
            if not user.check_password(password):raise CustomError("Wrong Password")

            else:attrs['user'] = user
        return attrs


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[],required=False)
    first_name= serializers.CharField(validators=[],required=False)
    last_name= serializers.CharField(validators=[],required=False)
    password= serializers.CharField(validators=[],required=False)


    def create(self, validated_data):
        user= get_user_model().objects.create_user(
            **validated_data
        )
        user.save()


        return user

    def validate(self, attrs):
        email = attrs.get('email')
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        password = attrs.get('password')

  
        if email is None:
            raise CustomError(message=f'Email Must Not Be Empty')

        if get_user_model().objects.filter(email=email).exists():
            "this checks if the User exist"

            raise CustomError(message=f'This {email} already Exits!')

        if first_name is None or len(first_name) == 0:
            raise CustomError(message=f'first Name is required')

        if last_name is None or len(last_name) == 0:
            raise CustomError(message=f'Last Name is required')

        if password is None or len(password) == 0:
            raise CustomError(message=f'Password is required')

        return attrs





# class BlogSerializer(serializers.ModelSerializer):


#     class Meta:
#         model =models.BlogPosts
#         fields =('id','title','author','main_image',
#         'blogcontent_text',''
#         )
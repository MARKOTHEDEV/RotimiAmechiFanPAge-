from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager






class UserManager(BaseUserManager):
    "this is what will manage the user"

    def create_user(self,first_name,last_name,email,password=None):
        "this is a custom function used to create my custom user"

        if password is None:
            raise ValueError("You Need To enter A Valid Password")

        user = self.model(
            email = email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,first_name,last_name,email,password):
        # function create a normal user and convert it to a Super User
        user = self.create_user(first_name,last_name,email,password)
        
        user.is_staff = True
        user.is_superuser=True
        user.save()

        return user


class User(PermissionsMixin,AbstractBaseUser):
    'This is Our Custom User The Whole Project will Use'

    email =      models.EmailField(unique=True)
    first_name=  models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['first_name','last_name',]

    # now i want to link the custom UserManager to Help me manage this my custom user
    objects =UserManager()
 
    def __str__(self):
        return f'{self.full_name()}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'





















class News(models.Model):
    "In this Pane Users can upload News Article"
    image = models.ImageField(upload_to='newsImage/')
    heading = models.CharField(max_length=500)
    intro_content = models.TextField()


    def __str__(self):
        return self.heading
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

class RegisterData(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    state = models.CharField(max_length=200)
    local_govt = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Registered Data"
        verbose_name_plural = "Registered Data"


class BlogPosts(models.Model):
    is_approved=models.BooleanField(default=False)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='blogPost/')

    class Meta:
        verbose_name = "All Blog Posts"
        verbose_name_plural = "All Blog Posts"

    def __str__(self):
        return f'{self.title} by {self.author_name}'

class BlogContent(models.Model):
    blog_post = models.ForeignKey(BlogPosts,on_delete=models.CASCADE)
    text = models.TextField()



# blog:
#     title
#     author_name

# ContentBody
# blog = oneBlog should have multiple contentbody
# text =
# image =





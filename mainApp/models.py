from django.db import models



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
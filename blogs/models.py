from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Tag(models.Model):
    caption = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images', null=True,)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    date = models.DateField(auto_now=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.author} {self.date}'
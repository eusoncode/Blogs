from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'
    
class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption

class Post(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts')
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=150)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    excerpt = models.TextField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return f'{self.title} {self.author} {self.date}'
from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length= 250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    post_image = models.ImageField(upload_to= 'post/%Y/%m/%d')
    category = models.ForeignKey('Category', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now= False, auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True, auto_now_add= False)
    slug = models.SlugField(max_length= 250, null= True, blank= True)

    def __str__(self):
        return self.title + ' BY ' + str(self.author)

    def save(self, *args, **kwargs):
        self.slug= slugify(self.title)
        super(Article, self).save(*args, **kwargs)

class Category(models.Model):
    name= models.CharField(max_length= 250)
    slug= models.SlugField(max_length= 250, null= True, blank= True)

    class Meta:
        verbose_name= "Category"
        verbose_name_plural= "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super(Category, self).save(*args, **kwargs)

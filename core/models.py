from django.db import models


#Recipe, User, Story Comment Category, Tag, Contact, Subscriber

class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='files/')
    text = models.TextField()
    views = models.IntegerField(default=0)
    # category
    # tag
    # comment
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='files/')
    text = models.TextField()
    views = models.IntegerField(default=0)
    # category
    # tag
    # comment
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    # user
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='files/')

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
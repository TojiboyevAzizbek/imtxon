from django.db import models

# Banner uchun model
class Banner(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
    
# Avtoservis haqida model
class Avtoservis_haqida(models.Model):
    title = models.CharField(max_length=255, default = '')
    body = models.TextField()

    def __str__(self):
        return self.body
    

# xizmatlarimiz uchun model
class Xizmatlar(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='xizmatlar/')
    
    def __str__(self):
        return self.name


# Xodimlar uchun model 
class Xodimlarimiz(models.Model):
    name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='xodimlar/')
        
    def __str__(self):
        return self.name


# Aloqa uchun model
class Aloqa(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


# Blog uchun model
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='blog/')
# Create your models here.

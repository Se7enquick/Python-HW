from django.db import models
# Create your models here.


class Author(models.Model):
    author_name = models.CharField(max_length = 50)
    author_image = models.ImageField(null = True)
    author_email = models.EmailField(null = True, max_length = 255)  
      

class Category(models.Model):
    cat = models.CharField(default = 'category', max_length= 255)

class Video(models.Model):
    video_name = models.CharField(default = 'Video',max_length=200)
    desctiption_text = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    video_author = models.ForeignKey(Author, null = True, on_delete = models.CASCADE, related_name = 'user_video')
    video_cat = models.OneToOneField(Category, null=True, on_delete = models.CASCADE)

class Like(models.Model):
    author_of = models.ForeignKey(Author, null=True,max_length=50, on_delete = models.CASCADE, related_name = 'like_user')
    like_to = models.ForeignKey(Video,null=True, on_delete = models.CASCADE, related_name = 'video_like')

class Comment(models.Model):
    author_name = models.ForeignKey(Author,null=True, on_delete = models.CASCADE, related_name = 'user_name')
    comment_text = models.TextField(null=True, blank=True)
    comment_likes = models.OneToOneField(Like, null = True, on_delete= models.CASCADE)
    comment_to = models.ForeignKey(Video,null=True, on_delete = models.CASCADE, related_name = 'video_comment')

class Advertise(models.Model):
    ad = models.TextField(null= True)
    ad_to = models.ForeignKey(Video, null = True, on_delete = models.CASCADE, related_name= 'advertise_to_video')

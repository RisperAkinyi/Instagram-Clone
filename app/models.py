from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField



class Comments(models.Model):
    comment = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Images,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_comment(self):
        self.save()
    
    def delete_comments(self):
        self.delete()
        
    @classmethod
    def get_comment_by_image(cls,id):
        comment = Comments.objects.filter(image__pk = id)
        return comment
    
    
from django.db import models

# Create your models here.
class moviesdata(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    # api endpoints
    # type of movie we search that type of movie list should be shown
    typ = models.CharField(max_length=200,default="action")
    image = models.ImageField(upload_to='Images/',default="Images/None/noimage.jpg")
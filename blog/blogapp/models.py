from django.db import models

# Category model
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
#Blog model with Many to one relation with Category model
class Blog(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
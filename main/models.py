from django.db import models

# Create your models here.

class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
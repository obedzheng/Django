from django.db import models

# Create your models here.
class Article(models.Model):
    ID = models.AutoField(primary_key=True, verbose_name="PK")
    title = models.TextField(verbose_name="title", null=False)
    article = models.TextField(verbose_name="article with markdown format", null=False)
    author = models.CharField(max_length=64, verbose_name="author", null=False)
    create_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="date of create")
    update_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="date of last modify")
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
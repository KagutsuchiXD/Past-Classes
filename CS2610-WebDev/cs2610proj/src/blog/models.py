from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    post_content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_id = models.ForeignKey('Blog', on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    comment_content = models.EmailField(blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return self.username

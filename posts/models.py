from django.db import models

class Post(models. Model):
    title = models. CharField(max_length=100, verbose_name="Заголовок")
    content = models. TextField(max_length=500, verbose_name="Текст посту")
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models. DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-pub_date']

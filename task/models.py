from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    photo = models.ImageField(upload_to="")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Пост пользователя: {self.author.username}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Пользователь: {self.author.username}, прокомментировал ваш пост в {self.created_at}"


class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_dislike = models.BooleanField(default=False, null=True)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        # return f"{'Дизлайк' if self.is_dislike else 'Лайк'}, от {self.user.username}, для поста {self.post}"
        if self.is_dislike:
            return f"Dislike от {self.user.username} для поста {self.post}"
        else:
            return f"Like от {self.user.username} для поста {self.post}"

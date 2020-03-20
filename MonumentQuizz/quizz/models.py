from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import EXPERIENCE_EXP_INCREASE
from .constants import EXPERIENCE_CONSTANT


# Create your models here
class QuizzUser(AbstractUser):
    experience = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    def get_treshold(self):
        return EXPERIENCE_EXP_INCREASE * self.level + EXPERIENCE_CONSTANT

    def add_experience(self, monument, xp_count):
        self.experience += xp_count
        if self.experience >= self.get_treshold():
            self.level += 1
            self.experience = self.experience - self.get_treshold()

    def get_todo_monuments(self):
        done_user_monument = self.user_monuments.filter(done=True)
        return Monument.objects.exclude(user_monuments__in=done_user_monument)

    def register_done(self, monument):
        self.user_monuments.get(user=self, monument=monument).register_done()

class Monument(models.Model):
    image = models.ImageField(upload_to="img", null=False)
    city = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.pk:
            created = True
        monument = super().save(*args, **kwargs)
        if created:
            for user in QuizzUser.objects.all():
                UserMonument.objects.create(
                    monument_id=self.pk,
                    user_id=user.pk,
                )

class UserMonument(models.Model):
    user = models.ForeignKey(QuizzUser, on_delete=models.CASCADE, related_name='user_monuments')
    monument = models.ForeignKey(Monument, on_delete=models.CASCADE, related_name='user_monuments')
    done = models.BooleanField(default=False)

    def register_done(self):
        self.done = True
        return self.save()



        
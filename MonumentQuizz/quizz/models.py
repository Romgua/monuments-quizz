from django.db import models
from django.contrib.auth.models import AbstractUser
from quizz import constants

# Create your models here
class QuizzUser(AbstractUser):
    experience = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    # def save(self):
    #     exp_treshold = EXPERIENCE_EXP_INCREASE * self.level + EXPERIENCE_CONSTANT
    #     if self.experience >= exp_treshold:
    #         self.level += 1
    #         self.experience = self.experience - exp_treshold
    #     return super().save()

class Monument(models.Model):
    image = models.ImageField(upload_to="img", null=False)
    name = models.CharField(max_length=200)

class UserMonument(models.Model):
    user = models.ForeignKey(QuizzUser, on_delete=models.CASCADE)
    monument = models.ForeignKey(Monument, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)


        
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class skillAndExpertise(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=100)


    def __str__(self):
        return self.skills
    
    class Meta:
        permissions =[
            ("view_Skill_and_Expertise_model", "can view SkillAndExpertise model")
        ]

class EducationDetails(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    education = models.CharField(max_length=500)

    def __str__(self):
        return self.education
    
    class Meta:
        permissions =[
            ("view_EducationDetails_model", "can view Education model ")
        ]

class AwardDetails(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    award = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.award
    
    class Meta:
        permissions = [
            ("view_AwardDetails_Model", "can view Award Detail Model")
        ]
    

from django.shortcuts import render
from .models import skillAndExpertise, EducationDetails, AwardDetails
# Create your views here.

def index(request):
    if request.user.has_perm(['app1.view_Skill_and_Expertise_model', 'app1.view_EducationDetails_model', 'app1.view_AwardDetails_Model']):
        skill = skillAndExpertise.objects.all()
        educ = EducationDetails.objects.all()
        awards = AwardDetails.objects.all()
        return render(request, 'index.html', {'skill': skill, 
                                              'educ' : educ,
                                              'awards': awards})
    return render(request, 'index.html') 


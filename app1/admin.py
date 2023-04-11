from django.contrib import admin
from .models import skillAndExpertise, EducationDetails, AwardDetails

admin.site.register(skillAndExpertise)
admin.site.register(EducationDetails)
admin.site.register(AwardDetails)
class SkillAndExpertiseAdmin(admin.ModelAdmin):
    fields = ('owner','skills')

    def has_change_permission(self, request, obj = None):
        if obj is not None and obj.owner != request.user:
            return False

        else:
            return True
        
    def has_view_permission(self, request, obj = None):
        if request.user.has_perm('app1.view_Skill_and_Expertise_model'):
            return True
        else:
            return False
        
class EducationDetailsModel(admin.ModelAdmin):
    fields = ('owner,education')

    def has_change_permission(self, request, obj = None) -> bool:
        if obj is not None and obj.owner != request.user:
            return False
        else:
            return True
        
    def has_view_permission(self, request, obj=None) -> bool:
        if request.user.has_perm('app1.view_EducationDetails_model'):
            return True
        else:
            return False
        
class AwardDetailAdmin(admin.ModelAdmin):
    fields = "__all__"

    def has_change_permission(self, request, obj=None) -> bool:
        if obj is not None and obj.owner != request.user:
            return False
        else:
            return True
        
    def has_view_permission(self, request, obj=None) -> bool:
        if request.user.has_perm('app1.view_AwardDetails_Model'):
            return True
        else:
            return False

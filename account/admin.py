from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

 
class CustomUserAdmin(UserAdmin):
    """
        show model custom user at django admin
    """
    model=CustomUser
    list_display=("email","is_active","is_staff",)
    list_filter=("is_active","is_staff",)
    ordering=("date_join",)
    search_fields=("email",)
    fieldsets=(
        (None,{"fields":("email",)}),
          ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
     
    )
    add_fieldsets=(
        (None,{"classes":("wide",),"fields":("email","password1","password2","is_active","is_staff", "groups", "user_permissions")}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
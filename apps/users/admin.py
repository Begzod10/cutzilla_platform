from django.contrib import admin
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'telegram_id')

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password') and not obj.password.startswith('pbkdf2_'):
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)


admin.site.register(Users, UsersAdmin)

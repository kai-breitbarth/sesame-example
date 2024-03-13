from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    # Define custom fieldsets for the custom user model
    fieldsets = (
        (None, {"fields": ("email",)}),
        (_("Personal info"), {"fields": ()}),  # Add any additional fields here
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    # Define which fields are used to add a user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email",),
            },
        ),
    )
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)

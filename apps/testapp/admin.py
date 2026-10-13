from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.testapp.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "role", "is_verified", "is_active")
    list_filter = ("role", "is_verified", "is_active", "is_staff")
    search_fields = ("email", "username")
    ordering = ("-id",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Личная информация", {"fields": ("username", "phone", "avatar", "bio", "birth_date")}),
        (
            "Права доступа и статусы",
            {
                "fields": (
                    "role",
                    "is_verified",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "role",
                    "is_verified",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
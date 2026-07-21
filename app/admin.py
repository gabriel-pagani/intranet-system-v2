from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from .models import Users, GroupProxy, Setores, Ramais, Dashboards, GroupDashboards


# Users Admin
@admin.register(Users)
class UsersAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'is_active',)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'observations',)
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups',)
    filter_horizontal = ('groups', 'user_permissions', 'dashboards',)
    model = Users
    ordering = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password',)
        }),
        ('Informações pessoais', {
            'fields': ('first_name', 'last_name', 'email',)
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'dashboards',)
        }),
        ('Datas importantes', {
            'fields': ('last_login', 'date_joined',)
        }),
        ('Observações', {
            'fields': ('observations',)
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2',),
        }),
    )


# Groups Admin
admin.site.unregister(Group)
@admin.register(GroupProxy)
class GroupsAdmin(BaseGroupAdmin):
    ...


@admin.register(Setores)
class SetoresAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Ramais)
class RamaisAdmin(admin.ModelAdmin):
    list_display = ('get_display_name', 'phone', 'sector', 'machine',)
    search_fields = ('name', 'user__username', 'user__first_name', 'user__last_name', 'phone', 'sector__name', 'machine',)
    list_filter = ('sector',)
    autocomplete_fields = ('sector', 'user')


# Dashboards Admin
@admin.register(Dashboards)
class DashboardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'sector', 'status')
    search_fields = ('title', 'sector__name')
    filter_horizontal = ('fav_by',)
    list_filter = ('status', 'sector',)
    autocomplete_fields = ('sector',)

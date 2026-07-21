from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, Group
from django.core.exceptions import ValidationError


class Users(AbstractUser):
    email = models.EmailField(blank=True, null=True, verbose_name='Endereço de email')
    observations = models.TextField(blank=True, null=True, verbose_name='Observações')

    def clean(self):
        super().clean()
        if self.email:
            email = Users.objects.filter(email=self.email).exclude(pk=self.pk)
            if email.exists():
                raise ValidationError({'email': 'Já existe um usuário com este e-mail.'})


class GroupProxy(Group):
    class Meta:
        proxy = True
        verbose_name = Group._meta.verbose_name
        verbose_name_plural = Group._meta.verbose_name_plural
        app_label = 'app'


class Setores(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Setor')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'


class Ramais(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Usuário',
        related_name='ramais'
    )
    name = models.CharField(max_length=100, blank=True, verbose_name='Nome')
    phone = models.CharField(max_length=100, blank=True, verbose_name='Ramal')
    sector = models.ForeignKey(
        Setores,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Setor',
        related_name='ramais'
    )
    machine = models.CharField(max_length=100, blank=True, verbose_name='Máquina')

    @admin.display(description='Nome')
    def get_display_name(self):
        if self.user:
            return self.user.get_full_name() or self.user.username
        return self.name

    def __str__(self):
        return f'{self.get_display_name()} - {self.phone}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Ramal'
        verbose_name_plural = 'Ramais'

from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    """
    App base User class.

    Email and password are required. Others field are optional.
    """
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether ehte user can log into this admin site'),          
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        # Return te first_name
        full_name = '%s' % (self.first_name)
        return full_name.strip()
    
    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Morador(models.Model):
    
    DOCS = (
        ('RG', 'Registro Geral'),
        ('CPF', 'Cadastro de Pessoa Física'),
    )
    
    TRABALHA = (
        ('Sim', 'Trabalha'),
        ('Não', 'Não Trabalha'),
    )
    
    ESTUDA = (
        ('Sim', 'Estuda'),
        ('Não', 'Não Estuda'),
    )
    
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    
    PARENTESCO = (
        ('Esposo/a', 'Esposo/a'),
        ('Filho/a', 'Filho/a'),
        ('Irmão/ã', 'Filho/ã'),
        ('Avô/ó', 'Avô/ó'),
        ('Sobrinho/a', 'Sobrinho/a'),
        ('Neto/a', 'Neto/a'),
        ('Tio/a', 'Tio/a'),
        ('Primo/a', 'Primo/a'),
        ('Genro/Nora', 'Genro/Nora'),
        ('Outros', 'Outros')
    )
    
    nome_completo = models.CharField('Nome Completo', max_length=60)
    documento = models.CharField('Tipo de documento', max_length=10, choices=DOCS)
    n_documento = models.CharField('Número do documento', max_length=60)
    data_nascimento = models.DateTimeField('Data de nascimento')
    trabalhando = models.CharField('Sim ou Não', max_length=20, choices=TRABALHA)
    estudando = models.CharField('Tipo de documento', max_length=10, choices=ESTUDA)
    sexo = models.CharField('Tipo de documento', max_length=10, choices=SEXOS)
    grau_parentesco = models.CharField('Tipo de documento', max_length=10, choices=PARENTESCO)
    
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
    n_documento = models.IntegerField('Número do documento', max_length=11)
    data_nascimento = models.DateTimeField('Data de nascimento')
    trabalhando = models.CharField('Sim ou Não', max_length=20, choices=TRABALHA)
    estudando = models.CharField('Tipo de documento', max_length=10, choices=ESTUDA)
    sexo = models.CharField('Sexo', max_length=10, choices=SEXOS)
    grau_parentesco = models.CharField('Tipo de documento', max_length=10, choices=PARENTESCO)
    
    def __str__(self):
        return str(self.id)
    
    

class Anfitrião(models.Model):
    
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    
    ESTADO_CIVIL = (
        ('S', 'Solteiro/a'),
        ('C', 'Casado/a'),
        ('V', 'Viúvo/a'),
        ('S', 'Separado/a'),
        ('O', 'Outros'),
    )
    
    ESCOLARIDADE = (
        ('F', 'Fundamental'),
        ('M', 'Médio'),
        ('SI', 'Superior Inc.'),
        ('SC', 'Superior Completo'),
        ('S', 'Sem escolaridade'),
    )
    
    RESIDENCIA = (
        ('P', 'Própria'),
        ('A', 'Alugada'),
        ('M', 'Moro com Parentes'),
        ('O', 'Outro'),
    )
    
    SITUACAO_ATUAL = (
        ('T', 'Trabalhando'),
        ('D', 'Desempregado'),
        ('Af', 'Afastado'),
        ('Ap', 'Aposentado'),
        ('P', 'Pensionista'),
        ('O', 'Outros'),
    )
    
    RELIGIAO = (
        ('C', 'Católico'),
        ('E', 'Evangélico'),
        ('O', 'Outra'),
    )
    
    PRATICANTE = (
        ('S', 'Sim'),
        ('N', 'Não'),
        ('A', 'As vezes'),
    )
    
    FILHOS = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    
    ALGUEM = (
        ('D', 'Doente'),
        ('DF', 'Def. Físico'),
        ('N', 'Não'),
    )
    
    SAUDE = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    
    AUXILIO = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    
    nome_completo = models.CharField('Nome Completo', max_length=60)
    data_nascimento = models.DateField('Data de nascimento')
    rg = models.DecimalField('Número do RG', max_digits=7, decimal_places=0, null=True)
    cpf = models.DecimalField('Número do CPF', max_digits=11, decimal_places=0, null=True)
    data_casamento = models.DateField('Data de casamento', null=True)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXOS, default='M')
    nome_pai = models.CharField('Nome do Pai', max_length=60)
    nome_mãe = models.CharField('Nome da Mãe', max_length=60)
    naturalidade = models.CharField('Cidade de origem', max_length=60)
    estado_civil = models.CharField('Estado civil', max_length=17, choices=ESTADO_CIVIL, default='C')
    escolaridade = models.CharField('Escolaridade', max_length=17, choices=ESCOLARIDADE, default='F')
    telefone = models.IntegerField('Celular ou Telefone', null=True)
    profissao = models.CharField('Profissão', max_length=60)
    n_carteira_trabalho = models.IntegerField('Nº Careteira de Trabalho', null=True)
    situacao_atual = models.CharField('Situação atual', max_length=17, choices=SITUACAO_ATUAL, default='T')
    religiao = models.CharField('Religião', max_length=17, choices=RELIGIAO, default='C')
    praticante = models.CharField('Praticante', max_length=17, choices=PRATICANTE, default='S')
    filhos = models.CharField('Possui filhos', max_length=17, choices=FILHOS, default='S')
    n_filhos = models.CharField('Se possuir filhos, informar o Nº', max_length=17, null=True)
    filhos_residencia = models.CharField('Se possuir filhos, informar quantos moram junto', max_length=17, null=True)
    filhos_menor_quartorze_anos = models.CharField('Se possuir filhos, informar se possui filhos menores de 14 anos', max_length=17, null=True)
    alguem_impossibilitado = models.CharField('Na família tem alguém:', max_length=17, choices=ALGUEM, default='D')         
    tipo_doenca = models.CharField('Se tiver alguém doente, informar o tipo de doença', max_length=17, null=True)
    tipo_deficiencia = models.CharField('Se tiver alguém deficiente, informar o tipo da deficiência', max_length=17, null=True)    
    alguem_posto_saude = models.CharField('Alguém frequenta posto de saúde?', max_length=17, choices=SAUDE, default='S')
    posto_bairro = models.CharField('Se alguém frequentar o posto, informar o posto e o bairro', max_length=17, null=True)
    alguem_beneficio_auxilio = models.CharField('Alguém recebe algum benefício/auxílio do governo?', max_length=17, choices=AUXILIO, default='S')
    beneficio_auxilio = models.CharField('Se alguém receber algum auxilio/beneficio do governo, informar-lo', max_length=17, null=True)
    tipo_residencia = models.CharField('Tipo de Residência', max_length=17, choices=RESIDENCIA, default='A')
    endereco = models.CharField('Av/Rua do endereço', max_length=100, null=True)
    n_endereco = models.CharField('Nº do endereço', max_length=30, null=True)
    comp_endereco = models.CharField('Se tiver complemento do endereço', max_length=50, null=True)
    bairro = models.CharField('Bairro', max_length=70, null=True)
    cidade = models.CharField('Cidade', max_length=70, null=True)
    estado = models.CharField('Estado', max_length=70, null=True)
    
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'Família'
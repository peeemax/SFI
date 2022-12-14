from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
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


class User(AbstractBaseUser, PermissionsMixin):
    """
    App base User class.
    Email and password are required. Other fields are optional.
    """

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s' % (self.first_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Anfitri??o(models.Model):
    
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('Outro', 'Outro'),
    )
    
    ESTADO_CIVIL = (
        ('S', 'Solteiro/a'),
        ('C', 'Casado/a'),
        ('V', 'Vi??vo/a'),
        ('S', 'Separado/a'),
        ('O', 'Outros'),
    )
    
    ESCOLARIDADE = (
        ('F', 'Fundamental'),
        ('M', 'M??dio'),
        ('SI', 'Superior Inc.'),
        ('SC', 'Superior Completo'),
        ('S', 'Sem escolaridade'),
    )
    
    RESIDENCIA = (
        ('P', 'Pr??pria'),
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
        ('C', 'Cat??lico'),
        ('E', 'Evang??lico'),
        ('O', 'Outra'),
    )
    
    PRATICANTE = (
        ('S', 'Sim'),
        ('N', 'N??o'),
        ('A', 'As vezes'),
    )
    
    FILHOS = (
        ('S', 'Sim'),
        ('N', 'N??o'),
    )
    
    ALGUEM = (
        ('D', 'Doente'),
        ('DF', 'Def. F??sico'),
        ('N', 'N??o'),
    )
    
    SAUDE = (
        ('S', 'Sim'),
        ('N', 'N??o'),
    )
    
    AUXILIO = (
        ('S', 'Sim'),
        ('N', 'N??o'),
    )
    
    nome_completo = models.CharField('Nome Completo', max_length=60)
    data_nascimento = models.DateField('Data de nascimento')
    rg = models.IntegerField('N??mero do RG', max_length=7, blank=True, null=True)
    cpf = models.IntegerField('N??mero do CPF', max_length=11, blank=True, null=True)
    data_casamento = models.DateField('Data de casamento', null=True, blank=True)
    sexo = models.CharField('Sexo', max_length=10, choices=SEXOS, default='M')
    nome_pai = models.CharField('Nome do Pai', max_length=60)
    nome_m??e = models.CharField('Nome da M??e', max_length=60)
    naturalidade = models.CharField('Cidade de origem', max_length=60)
    estado_civil = models.CharField('Estado civil', max_length=17, choices=ESTADO_CIVIL, default='C')
    escolaridade = models.CharField('Escolaridade', max_length=17, choices=ESCOLARIDADE, default='F')
    telefone = models.IntegerField('Celular ou Telefone', null=True)
    n_carteira_trabalho = models.IntegerField('N?? Carteira de Trabalho', blank=True, null=True)
    situacao_atual = models.CharField('Situa????o atual', max_length=17, choices=SITUACAO_ATUAL, default='T')
    profissao = models.CharField('Profiss??o', max_length=60, null=True, blank=True)
    religiao = models.CharField('Religi??o', max_length=17, choices=RELIGIAO, default='C')
    praticante = models.CharField('Praticante', max_length=17, choices=PRATICANTE, default='S')
    filhos = models.CharField('Possui filhos', max_length=17, choices=FILHOS, default='S')
    n_filhos = models.CharField('Se possuir filhos, informar o N??', max_length=17, blank=True, null=True)
    filhos_residencia = models.CharField('Se possuir filhos, informar quantos moram junto', max_length=17, blank=True, null=True)
    filhos_menor_quartorze_anos = models.CharField('Se possuir filhos, informar se possui filhos menores de 14 anos', max_length=17, blank=True, null=True)
    alguem_impossibilitado = models.CharField('Na fam??lia tem algu??m:', max_length=17, choices=ALGUEM, default='D')         
    tipo_doenca = models.CharField('Se tiver algu??m doente, informar o tipo de doen??a', max_length=17, blank=True, null=True)
    tipo_deficiencia = models.CharField('Se tiver algu??m deficiente, informar o tipo da defici??ncia', max_length=17, blank=True, null=True)    
    alguem_posto_saude = models.CharField('Algu??m frequenta posto de sa??de?', max_length=17, choices=SAUDE, default='S')
    posto_bairro = models.CharField('Se algu??m frequentar o posto, informar o posto e o bairro', max_length=17, blank=True, null=True)
    alguem_beneficio_auxilio = models.CharField('Algu??m recebe algum benef??cio/aux??lio do governo?', max_length=17, choices=AUXILIO, default='S')
    beneficio_auxilio = models.CharField('Se algu??m receber algum auxilio/beneficio do governo, informar-lo', max_length=17, blank=True, null=True)
    n_pessoas_familia = models.CharField('Quantas pessoas possuem na fam??lia (contando com o anfitri??o).', max_length=17)
    tipo_residencia = models.CharField('Tipo de Resid??ncia', max_length=17, choices=RESIDENCIA, default='A')
    endereco = models.CharField('Av/Rua do endere??o', max_length=100, null=True)
    n_endereco = models.CharField('N?? do endere??o', max_length=30, null=True)
    comp_endereco = models.CharField('Se tiver complemento do endere??o', max_length=50, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=70, null=True)
    cep = models.CharField('CEP', max_length=70, null=True)
    cidade = models.CharField('Cidade', max_length=70, null=True)
    estado = models.CharField('Estado', max_length=70, null=True)
    
    
    def __str__(self):
        return str(self.nome_completo)
    
    class Meta:
        ordering = ['nome_completo']
       
class Morador(models.Model):
    
    DOCS = (
        ('RG', 'Registro Geral'),
        ('CPF', 'Cadastro de Pessoa F??sica'),
    )
    
    TRABALHA = (
        ('Sim', 'Trabalha'),
        ('N??o', 'N??o Trabalha'),
    )
    
    ESTUDA = (
        ('Sim', 'Estuda'),
        ('N??o', 'N??o Estuda'),
    )
    
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('Outro', 'Outro'),
        
    )
    
    PARENTESCO = (
        ('Esposo/a', 'Esposo/a'),
        ('Pai', 'Pai'),
        ('M??e', 'M??e'),
        ('Filho/a', 'Filho/a'),
        ('Irm??o/??', 'Irm??o/??'),
        ('Av??/??', 'Av??/??'),
        ('Sobrinho/a', 'Sobrinho/a'),
        ('Neto/a', 'Neto/a'),
        ('Tio/a', 'Tio/a'),
        ('Primo/a', 'Primo/a'),
        ('Genro/Nora', 'Genro/Nora'),
        ('Outros', 'Outros')
    )
    
    nome_completo = models.CharField('Nome Completo', max_length=60)
    documento = models.CharField('Tipo de documento', max_length=10, choices=DOCS)
    n_documento = models.IntegerField('N??mero do documento', max_length=11)
    data_nascimento = models.DateField('Data de nascimento')
    sexo = models.CharField('Sexo', max_length=10, choices=SEXOS)
    trabalhando = models.CharField('Trabalha?', max_length=20, choices=TRABALHA)
    estudando = models.CharField('Estuda?', max_length=10, choices=ESTUDA)
    grau_parentesco = models.CharField('Qual grau de parentesco?', max_length=10, choices=PARENTESCO)
    anfitriao= models.ForeignKey(Anfitri??o, related_name='moradores', on_delete=models.CASCADE)

    
    def __str__(self):
        return str(self.nome_completo)
    
    
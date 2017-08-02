import re
import socket, struct

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CharField, DateTimeField
from django.db.models.fields import GenericIPAddressField, BigIntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver


def validate_MAC(value):
    if not re.match('^([0-9A-F]{2}:){5}[0-9A-F]{2}$', value.upper()):
        raise ValidationError('Esta no es una dirección MAC válida')


class Usuario(models.Model):
    nombre = CharField(max_length=255, null=True, blank=True)
    mac = CharField(max_length=17, unique=True, validators=[validate_MAC, ], null=True, blank=True)
    fecha_registro = DateTimeField(null=True, blank=True)
    responsable = CharField(max_length=255, null=True, blank=True)
    telefono = CharField(max_length=255, null=True, blank=True)
    zona = CharField(max_length=255, null=True, blank=True)
    tipo = CharField(max_length=255, null=True, blank=True)
    ip = GenericIPAddressField(unique=True)
    ip_int = BigIntegerField(default=0)

    def __str__(self):
        if self.nombre:
            return self.nombre + '(' + self.ip + ')'
        else:
            return self.ip


@receiver(post_save, sender=Usuario)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.ip_int != ip_to_int(instance.ip):
        instance.ip_int = ip_to_int(instance.ip)
        instance.save()


def ip_to_int(ip):
    try:
        return struct.unpack('!I', socket.inet_pton(socket.AF_INET, ip))[0]
    except socket.error:
        try:
            hi, lo = struct.unpack('!QQ', socket.inet_pton(socket.AF_INET6, ip))
            return (hi << 64) | lo
        except socket.error:
            return 0

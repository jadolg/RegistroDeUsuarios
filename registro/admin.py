from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group
from registro.models import Usuario, Zona, Responsable, TipoDeEquipo


class UsuarioAdmin(admin.ModelAdmin):
    def responsable_equipo(self, obj):
        if obj.responsable:
            return '<a href="http://localhost:8000/admin/registro/responsable/' + str(obj.responsable.id) + '/change/">' \
                   + obj.responsable.responsable + '</a>'
        else:
            return "-"

    responsable_equipo.allow_tags = True

    list_display = ('nombre', 'ip', 'mac', 'fecha_registro', 'responsable_equipo', 'telefono', 'zona', 'tipo',)
    search_fields = ('nombre', 'ip', 'mac', 'fecha_registro', 'responsable__responsable', 'telefono', 'zona__zona', 'tipo__tipo',)
    list_filter = ('responsable', 'zona', 'tipo')
    ordering = ('ip_int',)

    exclude = ('ip_int',)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Zona)
admin.site.register(Responsable)
admin.site.register(TipoDeEquipo)
# admin.site.unregister(User)
admin.site.unregister(Group)

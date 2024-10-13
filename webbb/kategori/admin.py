from django.contrib import admin

# Register your models here.
from . models import Kategori,Besin

fields = ['kategori', 'name', 'protein', 'yağ', 'karbonhidrat', 'kalori']
# Register your models here.


class BesinInline(admin.TabularInline):
    model = Besin
    extra = 1

class KategoriAdmin(admin.ModelAdmin):
    inlines = [BesinInline]

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Besin)
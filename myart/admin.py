from django.contrib import admin

# Register your models here.

from .models import Artist, Artwork, Exhibition, Owner, Showroom

@admin.register(Artist)
class TemplateArtistManager(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birthday', 'birthplace', 'bio', 'edu')

@admin.register(Artwork)
class TemplateArtworkManager(admin.ModelAdmin):
    list_display = ('title', 'author', 'medium', 'size', 'creation_day')
  
@admin.register(Owner)
class TemplateOwnerManager(admin.ModelAdmin):
    list_display = ('name', 'status', 'phone', 'address')
    
@admin.register(Showroom)
class TemplateShowroomManager(admin.ModelAdmin):
    list_display = ('name', 'area', 'address', 'phone', 'o')
  
@admin.register(Exhibition)
class TemplateExhibitionManager(admin.ModelAdmin):
    list_display = ('edate', 'etype', 'place')

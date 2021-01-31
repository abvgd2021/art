from django import forms
from .models import Artist, Owner, Artwork, Showroom

class ArtistForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    birthday = forms.DateField()
    birthplace = forms.CharField(max_length=20)
    bio = forms.CharField(widget=forms.Textarea, max_length=500)
    edu = forms.CharField(max_length=100)
    
class ArtworkForm(forms.Form):
    title = forms.CharField(max_length=50)
    size = forms.CharField(max_length=20)
    creation_day = forms.DateField()
    medium = forms.ChoiceField(choices=(('Краски','Краски'), ('Акварель','Акварель'), ('Скульптура','Скульптура')))
    author = forms.ModelChoiceField(queryset=Artist.objects.all())
    
class OwnerForm(forms.Form):
    name = forms.CharField(max_length=20)
    status = forms.ChoiceField(choices=(('гос','государственное'), ('мун','муниципальное'), ('част','частное')))
    phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=50)
    
class ShowroomForm(forms.Form):
    name = forms.CharField(max_length=50)
    area = forms.FloatField()
    phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=50)
    o = forms.ModelChoiceField(queryset=Owner.objects.all())
    
class ExhibitionForm(forms.Form):
    edate = forms.DateField()
    etype = forms.ChoiceField(choices=(('Картины','Картины'), ('Пр. искусство','Прикладное искусство'), ('Скульптура','Скульптура')))
    artworks = forms.ModelMultipleChoiceField(queryset=Artwork.objects.all())
    place = forms.ModelChoiceField(queryset=Showroom.objects.all())
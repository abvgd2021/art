from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# Create your views here.

from .forms import ArtistForm, ArtworkForm, OwnerForm, ShowroomForm, ExhibitionForm
from .models import Artist, Artwork, Owner, Showroom, Exhibition

def index(request):
    return render(request, "index.html")

class viewArtistManagement():

    def addArtist(request):
        if request.method == "POST":
            artist = Artist()
            artist.first_name = request.POST.get("first_name")
            artist.last_name = request.POST.get("last_name")
            artist.birthday = request.POST.get("birthday")
            artist.birthplace = request.POST.get("birthplace")
            artist.bio = request.POST.get("bio")
            artist.edu = request.POST.get("edu")
            artist.save()
        aform = ArtistForm()
        artists = Artist.objects.all()
        return render(request, "addArtist.html", {"form": aform, "artists": artists})
    
    def editArtist(request, id):
        try:
            artist = Artist.objects.get(id=id)
 
            if request.method == "POST":
                artist.first_name = request.POST.get("first_name")
                artist.last_name = request.POST.get("last_name")
                artist.birthday = request.POST.get("birthday")
                artist.birthplace = request.POST.get("birthplace")
                artist.bio = request.POST.get("bio")
                artist.edu = request.POST.get("edu")
                artist.save()
                return HttpResponseRedirect("/artist/")
            else:
                data = {'first_name': artist.first_name, 'last_name': artist.last_name, 'birthday': artist.birthday, 'birthplace': artist.birthplace, 'bio': artist.bio, 'edu': artist.edu}
                aform = ArtistForm(data)
                return render(request, "edit.html", {"form": aform})
        except Artist.DoesNotExist:
            return HttpResponseNotFound("<h2>artist not found</h2>")

    def deleteArtist(request, id):
        try:
            artist = Artist.objects.get(id=id)
            artist.delete()
            return HttpResponseRedirect("/artist/")
        except Artist.DoesNotExist:
            return HttpResponseNotFound("<h2>Artist not found</h2>")
        
class viewArtworkManagement():

    def addArtwork(request):
        if request.method == "POST":
            artwork = Artwork()
            artwork.title = request.POST.get("title")
            artwork.creation_day = request.POST.get("creation_day")
            artwork.size = request.POST.get("size")
            artwork.medium = request.POST.get("medium")
            artwork.author = Artist.objects.get(id=request.POST.get("author"))
            artwork.save()
        awform = ArtworkForm()
        artworks = Artwork.objects.all()
        return render(request, "addArtwork.html", {"form": awform, "artworks": artworks})
    
    def editArtwork(request, id):
        try:
            artwork = Artwork.objects.get(id=id)
 
            if request.method == "POST":
                artwork.title = request.POST.get("title")
                artwork.creation_day = request.POST.get("creation_day")
                artwork.size = request.POST.get("size")
                artwork.medium = request.POST.get("medium")
                artwork.author = Artist.objects.get(id=request.POST.get("author"))
                artwork.save()
                return HttpResponseRedirect("/artwork/")
            else:
                data = {'title': artwork.title, 'size': artwork.size, 'creation_day': artwork.creation_day, 'medium': artwork.medium, 'author': artwork.author}
                awform = ArtworkForm(data)
                return render(request, "edit.html", {"form": awform})
        except Artwork.DoesNotExist:
            return HttpResponseNotFound("<h2>Artwork not found</h2>")

    def deleteArtwork(request, id):
        try:
            artwork = Artwork.objects.get(id=id)
            artwork.delete()
            return HttpResponseRedirect("/artwork/")
        except Artwork.DoesNotExist:
            return HttpResponseNotFound("<h2>artwork not found</h2>")
        
class viewOwnerManagement():

    def addOwner(request):
        if request.method == "POST":
            owner = Owner()
            owner.name = request.POST.get("name")
            owner.status = request.POST.get("status")
            owner.phone = request.POST.get("phone")
            owner.address = request.POST.get("address")
            owner.save()
        oform = OwnerForm()
        owners = Owner.objects.all()
        return render(request, "addOwner.html", {"form": oform, "owners": owners})
    
    def editOwner(request, id):
        try:
            owner = Owner.objects.get(id=id)
 
            if request.method == "POST":
                owner.name = request.POST.get("name")
                owner.status = request.POST.get("status")
                owner.phone = request.POST.get("phone")
                owner.address = request.POST.get("address")
                owner.save()
                return HttpResponseRedirect("/owner/")
            else:
                data = {'name': owner.name, 'status': owner.status, 'phone': owner.phone, 'address': owner.address}
                oform = OwnerForm(data)
                return render(request, "edit.html", {"form": oform})
        except Owner.DoesNotExist:
            return HttpResponseNotFound("<h2>Owner not found</h2>")

    def deleteOwner(request, id):
        try:
            owner = Owner.objects.get(id=id)
            owner.delete()
            return HttpResponseRedirect("/owner/")
        except Owner.DoesNotExist:
            return HttpResponseNotFound("<h2>Owner not found</h2>")

class viewShowroomManagement():

    def addShowroom(request):
        if request.method == "POST":
            showroom = Showroom()
            showroom.name = request.POST.get("name")
            showroom.area = request.POST.get("area")
            showroom.phone = request.POST.get("phone")
            showroom.address = request.POST.get("address")
            showroom.o = Owner.objects.get(id=request.POST.get("o"))
            showroom.save()
        shform = ShowroomForm()
        showrooms = Showroom.objects.all()
        return render(request, "addShowroom.html", {"form": shform, "showrooms": showrooms})
    
    def editShowroom(request, id):
        try:
            showroom = Showroom.objects.get(id=id)
 
            if request.method == "POST":
                showroom.name = request.POST.get("name")
                showroom.area = request.POST.get("area")
                showroom.phone = request.POST.get("phone")
                showroom.address = request.POST.get("address")
                showroom.o = Owner.objects.get(id=request.POST.get("o"))
                showroom.save()
                return HttpResponseRedirect("/showroom/")
            else:
                data = {'name': showroom.name, 'area': showroom.area, 'phone': showroom.phone, 'address': showroom.address, 'o': showroom.o}
                shform = ShowroomForm(data)
                return render(request, "edit.html", {"form": shform})
        except Showroom.DoesNotExist:
            return HttpResponseNotFound("<h2>Showroom not found</h2>")

    def deleteShowroom(request, id):
        try:
            showroom = Showroom.objects.get(id=id)
            showroom.delete()
            return HttpResponseRedirect("/showroom/")
        except Showroom.DoesNotExist:
            return HttpResponseNotFound("<h2>Showroom not found</h2>")
        
class viewExhibitionManagement():

    def addExhibition(request):
        if request.method == "POST":
            exhibition = Exhibition()
            exhibition.edate = request.POST.get("edate")
            exhibition.etype = request.POST.get("etype")
            exhibition.place = Showroom.objects.get(id=request.POST.get("place"))
            exhibition.save()
            s = request.POST.getlist("artworks")
            for i in s:
                aw = Artwork.objects.get(id=int(i))
                exhibition.artworks.add(aw)   
        eform = ExhibitionForm()
        exhibitions = Exhibition.objects.all()
        return render(request, "addExhibition.html", {"form": eform, "exhibitions": exhibitions})
    
    def editExhibition(request, id):
        try:
            exhibition = Exhibition.objects.get(id=id)
 
            if request.method == "POST":
                exhibition.edate = request.POST.get("edate")
                exhibition.etype = request.POST.get("etype")
                exhibition.place = Showroom.objects.get(id=request.POST.get("place"))
                exhibition.save()
                exhibition.artworks.clear()
                s = request.POST.getlist("artworks")
                for i in s:
                    aw = Artwork.objects.get(id=i)
                    exhibition.artworks.add(aw)
                return HttpResponseRedirect("/exhibition/")
            else:
                data = {'edate': exhibition.edate, 'etype': exhibition.etype, 'artworks': exhibition.artworks, 'place': exhibition.place}
                eform = ExhibitionForm(data)
                return render(request, "edit.html", {"form": eform})
        except Exhibition.DoesNotExist:
            return HttpResponseNotFound("<h2>Exhibiton not found</h2>")

    def deleteExhibition(request, id):
        try:
            exhibition = Exhibition.objects.get(id=id)
            exhibition.delete()
            return HttpResponseRedirect("/exhibition/")
        except Exhibition.DoesNotExist:
            return HttpResponseNotFound("<h2>Exhibiton not found</h2>")
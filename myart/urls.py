from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('artist/editArtist/<int:id>/', views.viewArtistManagement.editArtist, name='editArtist'),
    path('artist/deleteArtist/<int:id>/', views.viewArtistManagement.deleteArtist, name='deleteArtist'),
    path('artist/', views.viewArtistManagement.addArtist, name='addArtist'),
    path('artwork/editArtwork/<int:id>/', views.viewArtworkManagement.editArtwork, name='editArtwork'),
    path('artwork/deleteArtwork/<int:id>/', views.viewArtworkManagement.deleteArtwork, name='deleteArtwork'),
    path('artwork/', views.viewArtworkManagement.addArtwork, name='addArtwork'),
    path('owner/editOwner/<int:id>/', views.viewOwnerManagement.editOwner, name='editOwner'),
    path('owner/deleteOwner/<int:id>/', views.viewOwnerManagement.deleteOwner, name='deleteOwner'),
    path('owner/', views.viewOwnerManagement.addOwner, name='addOwner'),
    path('showroom/editShowroom/<int:id>/', views.viewShowroomManagement.editShowroom, name='editShowroom'),
    path('showroom/deleteShowroom/<int:id>/', views.viewShowroomManagement.deleteShowroom, name='deleteShowroom'),
    path('showroom/', views.viewShowroomManagement.addShowroom, name='addShowroom'),
    path('exhibition/editExhibition/<int:id>/', views.viewExhibitionManagement.editExhibition, name='editExhibition'),
    path('exhibition/deleteExhibition/<int:id>/', views.viewExhibitionManagement.deleteExhibition, name='deleteExhibition'),
    path('exhibition/', views.viewExhibitionManagement.addExhibition, name='addExhibition'),
]
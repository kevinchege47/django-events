"""myclub_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [

    path('', views.home,name="home"),
    path('<int:year>/<str:month>/', views.home,name="home"),
    path('events',views.all_events,name="list-events"),
    path('add_venue',views.add_venue,name ="add-venue"),
    path('list_venues',views.list_venues,name ="list-venues"),
    path('show_venue/<venue_id>',views.show_venue,name="show-venue"),
    path('search_venues',views.search_venues,name="search-venues"),
    path('update_venue/<venue_id>',views.update_venue,name="update-venue"),
    path('add_event',views.add_event,name ="add-event"),
    path('update_event/<venue_id>',views.update_event,name="update-event"),
    path('delete_event/<event_id>',views.delete_event,name="delete-event"),
    path('delete_venue/<venue_id>',views.delete_venue,name="delete-venue"),
    
]

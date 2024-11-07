"""
URL configuration for Eco_Friendly_living project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path


# Importing views

from Carbon_Footprint_Tracker import views as CFT_views
from Community_composting import views as CC_views
from Dashboard import views as D_views
from Ecofriendly_Product_Finder import views as EPF_views
from Zero_Waste_Challenge import views as ZWC_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", D_views.home, name="home"),
    
    #Auth

    path("signup", D_views.signup_view, name="signup"),
    path("login", D_views.login_view, name="login"),
    path("logout", D_views.logout_view, name="logout"),

    path("dashboard", D_views.dashboard, name="dashboard"),



    # Community composting

    path("community_composting", CC_views.CC_Home, name="CC_Home"),
    

    #i) Discussions

    path('discussions/', CC_views.discussion_list, name='discussion_list'),
    path('discussions/create/', CC_views.create_discussion, name='create_discussion'),
    path('discussions/<int:discussion_id>/reply/', CC_views.create_reply, name='create_reply'),
    path('discussions/<int:discussion_id>/delete/', CC_views.delete_discussion, name='delete_discussion'),

    # ii) Finding Pits
    
    path('find-composting-pits/', CC_views.find_composting_pits, name='find_composting_pits'),
    path('add-composting-pit/', CC_views.add_composting_pit, name='add_composting_pit'),
    path('remove-composting-pit/<int:pit_id>/', CC_views.remove_composting_pit, name='remove_composting_pit'),

]

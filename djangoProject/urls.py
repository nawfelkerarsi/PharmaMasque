"""djangoProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from pharmamasque import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path("admin/", admin.site.urls),
    path("page/", views.page, name='page'),
    path("produits/", views.produits, name='produits'),
    path('produits/<int:page>/', views.produits, name='produits'),
    path("masques/", views.masques, name='masques'),
    path('masques/<int:page>/', views.masques, name='masques'),
    path("autotests/", views.autotests, name='autotests'),
    path('autotests/<int:page>/', views.autotests, name='autotests'),
    path("tests-antigéniques/", views.tests_antigeniques, name='tests-antigeniques'),
    path('tests-antigéniques/<int:page>/', views.tests_antigeniques, name='tests-antigeniques'),
    path("masques-chirurgicaux-adultes/", views.masques_chirurgicaux_adultes, name='masques-chirurgicaux-adultes'),
    path('masques-chirurgicaux-adultes/<int:page>/', views.masques_chirurgicaux_adultes, name='masques-chirurgicaux-adultes'),
    path("masques-chirurgicaux-enfants/", views.masques_chirurgicaux_enfants, name='masques-chirurgicaux-enfants'),
    path('masques-chirurgicaux-enfants/<int:page>/', views.masques_chirurgicaux_enfants, name='masques-chirurgicaux-enfants'),
    path("masques-ffp2/", views.masques_ffp2, name='masques-ffp2'),
    path('masques-ffp2/<int:page>/', views.masques_ffp2, name='masques-ffp2'),
    path("produit/<int:id_produit>/", views.produit, name='produit'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mon-compte/', views.mon_compte, name='mon-compte'),
    path('mon-compte/dernières-commandes/', views.dernieres_commandes, name='dernière-commandes'),
    path('ma-compagnie/<int:id_compagnie>/', views.ma_compagnie, name='ma-compagnie'),
    path('ma-compagnie/<int:id_compagnie>/dernières-commandes/', views.ma_compagnie__dernieres_commandes, name='ma-compagnie/dernière-commande'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/clients/', views.dashboard__clients, name="dashboard/clients"),
    path('dashboard/commandes/', views.dashboard__commandes, name="dashboard/commandes"),
    path('dashboard/articles/', views.dashboard__articles, name="dashboard/articles"),
    path('dashboard/livraisons/', views.dashboard__livraisons, name="dashboard/livraisons"),
    path('dashboard/adresses/', views.dashboard__adresses, name="dashboard/adresses"),
    path('dashboard/rapports/', views.dashboard__rapports, name="dashboard/rapports")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


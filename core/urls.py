from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='urlindex' ),
    path('analise01', views.line_chart_view, name='urlanalise01' ),
    path('analise02', views.bar_chart_view, name='urlanalise02'),
    path('analise03', views.pie_chart_view, name='urlanalise03'),
]
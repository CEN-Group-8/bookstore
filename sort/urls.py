from django.urls import path, re_path
from .views import SearchResultsView, browse_results_view, browse_by_category, top_10_sellers, top_20_sellers, rating5, rating4, rating3, rating2,rating1, SortResultsView, sort
from . import views

urlpatterns = [

    path(r'?P<catetgory>', views.browse_by_category, name='browse_by_category'),
    path(r'top10sellers', views.top_10_sellers, name='top_10_sellers'),
    path(r'top20sellers/', views.top_20_sellers, name='top_20_sellers'),
    re_path(r'^top20sellers/(?:page(?P<page>\d+))/', views.top_20_sellers, name='top_20_sellers'),
    path('rating5/', views.rating5, name='rating5'),
    path('rating4/', views.rating4, name='rating4'),
    path('rating3/', views.rating3, name='rating3'),
    path('rating2/', views.rating2, name='rating2'),
    path('rating1/', views.rating1, name='rating1'),
    path('searchView/', views.searchview, name= 'searchView'),
    path('sortBy/', views.sort, name='sort'),
    path(r'', views.browse_results_view, name='BroweseResultsView'),
    path(r'search/', SearchResultsView.as_view(), name='SearchResultsView'),
    
  
]
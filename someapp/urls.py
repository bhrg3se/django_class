from django.urls import path
from someapp import views
from someapp import consumers


urlpatterns = [
    path('index/',views.index),
    path('profile/<str:name>/',views.profile),
    path('add/',views.add),
    path('submit/',views.submit),
    path('addcomment/',views.addComment),
    path('viewcomments/',views.showComments),
    path('deletecomment/',views.delComment),
    path('someform/',views.someform)



]

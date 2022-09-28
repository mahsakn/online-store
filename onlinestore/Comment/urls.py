from django.urls import path

from Comment.views import comment

app_name = 'Comment'

urlpatterns = [
    path('publish_comment/<int:product_id>/', comment, name='commentproduct'),
]

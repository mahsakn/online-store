from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from Comment.forms import Comment
from Comment.models import CommentMe


@login_required(login_url="/user/login/")
def comment(request, product_id):

    if (request.method == 'POST'):
        commentform = Comment(request.POST)
        if commentform.is_valid():
            obj_comment = CommentMe.objects.create(
                user=request.user,
                product_id=product_id,
                comment=commentform.cleaned_data['comment']
            )
        return redirect("product:detailproduct", int(product_id))
    else:
        return redirect("product:detailproduct", int(product_id))

from django.shortcuts import render

from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import CommentForm

# Create your views here.
class CommentView(TemplateView):
    template_name = "comment/index.html"
    http_method_names = ['post']
    def post(self, request):
        comment_form = CommentForm(request.POST)
        target = request.POST.get("target")
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.target = target
            comment.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False
            
        context = {
            'form': comment_form,
            'target': target,
            'succeed': succeed
        }
        print(context['form'])
        return self.render_to_response(context)
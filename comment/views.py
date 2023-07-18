from django.shortcuts import render

from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import CommentForm

# Create your views here.
class CommentView(TemplateView):
    template_name = "comment/index.html"
    http_method_names = ['post']
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        taget = request.POST.get("target")
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.target = taget
            comment.save()
            succeed = True
            return redirect(taget)
        else:
            succeed = False
            
        context = {
            'form': comment_form,
            'target': taget,
            'succeed': succeed
        }
        print(context['form'])
        return self.render_to_response(context)
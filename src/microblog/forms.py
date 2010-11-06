from django.forms.models import ModelForm
from microblog.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ('user', )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(BlogForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        blog = super(BlogForm, self).save(*args, **kwargs)
        blog.user = self.user
        blog.save()
        return blog
        

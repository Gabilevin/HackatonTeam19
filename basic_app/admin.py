from django.contrib import admin
# Register your models here.

from django.contrib import admin
from basic_app.models import itemReviewToAdmin, stories_model




admin.site.register(itemReviewToAdmin)
admin.site.register(stories_model)





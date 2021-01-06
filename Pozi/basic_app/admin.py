from django.contrib import admin
from basic_app.models import  itemReviewToAdmin, stories_model, tip_model, QA_model,chat_first_question_model

# Register your models here.
from embed_video.admin import AdminVideoMixin
from .models import sport,motivation,stand_up


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(sport, MyModelAdmin)
admin.site.register(motivation, MyModelAdmin)
admin.site.register(stand_up, MyModelAdmin)

admin.site.register(QA_model)
admin.site.register(itemReviewToAdmin)
admin.site.register(stories_model)
admin.site.register(tip_model)
admin.site.register(chat_first_question_model)




from django.contrib import admin
from fundoonotes.models import Notes


class FundooNotesAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "done", "date_created")
    list_filter = ("done", "date_created")


admin.site.register(Notes, FundooNotesAdmin)

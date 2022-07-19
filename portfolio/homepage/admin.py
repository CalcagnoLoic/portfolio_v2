from django.contrib import admin
from homepage.models import AddProjects


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "titre", "description", "langage1", "langage2", "langage3", "langage4", "repository", "link_projet")


admin.site.register(AddProjects, ProjectsAdmin)

from django.db import models

def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.title), filename])

class file(models.Model): 
    title = models.CharField(max_length=32, blank=False)
    cover = models.FileField(blank=True, null=True, upload_to=upload_path)

    def __str__(self):
        return self.name
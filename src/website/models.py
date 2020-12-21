from django.db import models

# Create your models here.

class Recording(models.Model):
    uploaded_file = models.FileField()

    def __str__(self):
        return os.path.basename(self.uploaded_file.name)

    def delete(self, *args, **kwargs):
        self.uploaded_file.delete()
        super().delete(*args, **kwargs)
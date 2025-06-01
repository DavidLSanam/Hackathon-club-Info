from django.db import models

class FichierNotes(models.Model):
    fichier = models.FileField(upload_to='uploads/')
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fichier {self.fichier.name}"

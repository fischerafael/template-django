from django.db import models


class BragTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    brag = models.ForeignKey('Brag', on_delete=models.CASCADE)

    def __str__(self):
        return f"Tag: {self.tag.title} - Brag: {self.brag.title}"
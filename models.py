from django.db import models

class Settings(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
     return f"{self.name}: {self.value}"

# ini komentar percobaan
print(">>> MODELS.PY TERBACA <<<")
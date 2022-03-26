from django.db import models

# Create your models here.
class Persona(models.Model):
    """Model definition for Persona."""

    # TODO: Define fields here
    full_name = models.CharField("Nombres", max_length=50)
    country = models.CharField("Country", max_length=50)
    passport = models.CharField("Passport", max_length=50)
    age = models.IntegerField()
    ap = models.CharField("Appelative", max_length=10)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together = ["country","ap"]
        # Validate if age is great or equal to 18
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name="age_great_18")
        ]
        abstract = True

    def __str__(self):
        """Unicode representation of Persona."""
        return self.full_name

class Empleado(Persona):
    job = models.CharField("Job", max_length=50)

class Cliente(Persona):
    email = models.CharField("Email", max_length=50)

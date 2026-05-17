from django.db import models


# ─── PART 1: Base Model (Parent) ───────────────────────────────────────────

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def vehicle_info(self):
        """Base implementation — returns brand and price."""
        return f"{self.brand} costs {self.price:.0f}"

    def __str__(self):
        return self.vehicle_info()

    class Meta:
        # Makes Vehicle abstract so it doesn't create its own DB table;
        # each child model gets its own table instead.
        abstract = True


# ─── PART 2: Child Models ───────────────────────────────────────────────────

class Car(Vehicle):
    """Inherits from Vehicle. Adds doors field and overrides vehicle_info()."""
    doors = models.IntegerField(default=4)

    def vehicle_info(self):
        """Method overriding — Car-specific output."""
        return f"{self.brand} Car with {self.doors} doors costs {self.price:.0f}"

    def __str__(self):
        return self.vehicle_info()

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Motorcycle(Vehicle):
    """Inherits from Vehicle. Adds helmet_included field and overrides vehicle_info()."""
    helmet_included = models.BooleanField(default=False)

    def vehicle_info(self):
        """Method overriding — Motorcycle-specific output."""
        return f"{self.brand} Motorcycle costs {self.price:.0f}"

    def __str__(self):
        return self.vehicle_info()

    class Meta:
        verbose_name = "Motorcycle"
        verbose_name_plural = "Motorcycles"
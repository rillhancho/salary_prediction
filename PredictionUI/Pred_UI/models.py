from django.db import models

# Create your models here.

from django.db import models

class SalaryPrediction(models.Model):
    years_experience = models.FloatField()  # Field to store years of experience
    predicted_salary = models.FloatField()  # Field to store the predicted salary
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the prediction was made

    def __str__(self):
        return f"{self.years_experience} years - ${self.predicted_salary:.2f}"

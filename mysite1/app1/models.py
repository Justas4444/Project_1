from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class StockSymbol(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.symbol} - {self.company_name}"

    class Meta:
        verbose_name = "Stock Symbol"
        verbose_name_plural = "Stock Symbols"

class StockPrediction(models.Model):
    stock_symbol = models.ForeignKey(StockSymbol, on_delete=models.CASCADE)
    predicted_date = models.DateField()
    predicted_open = models.IntegerField(validators=[MaxValueValidator(9999)])
    predicted_high = models.IntegerField(validators=[MaxValueValidator(9999)])
    predicted_low = models.IntegerField(validators=[MaxValueValidator(9999)])
    predicted_close = models.IntegerField(validators=[MaxValueValidator(9999)])
    predicted_adjclose = models.IntegerField(validators=[MaxValueValidator(9999)])
    predicted_volume = models.IntegerField(validators=[MaxValueValidator(9999)])
    predicted_interest_rate = models.FloatField(default=0.0, validators=[MaxValueValidator(20)])

    def __str__(self):
        return f"{self.stock_symbol} - {self.predicted_date}: {self.predicted_open} : {self.predicted_high} : {self.predicted_low} : {self.predicted_close} : {self.predicted_adjclose} : {self.predicted_volume} : {self.predicted_interest_rate}"

    class Meta:
        verbose_name = "Stock Prediction"
        verbose_name_plural = "Stock Predictions"
        unique_together = ('stock_symbol', 'predicted_date' , 'predicted_open', 'predicted_high', 'predicted_low', 'predicted_close', 'predicted_adjclose', 'predicted_volume', 'predicted_interest_rate')

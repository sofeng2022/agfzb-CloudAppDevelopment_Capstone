from django.db import models
from django.utils.timezone import now


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100, default='Car')
    id = models.IntegerField(default=1,primary_key=True)
    
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
       
    ]

    type = models.CharField(
        null=False,
        max_length=50,
        choices=CAR_TYPES,
        default=SEDAN
    )
models.DateField(null=True)
def __str__(self):
    return "Name: " + self.name + "," + \
        "DealerId: " + self.dealer_id.__str__() + "," + \
            "Type: " + self.type + "," + \
                "Year: " + self.year.__str__()


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

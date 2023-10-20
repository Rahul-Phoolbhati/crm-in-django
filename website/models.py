from django.db import models

# DJANGO WILL Automatically convert to sql (if db is sql), django has db we need to migrate
# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField()
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    phone = models.CharField(max_length=15, default='N/A')  # Use 'N/A' as the default value
    address=models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=20)

    def __str__(self): # This means that when you call str() on an instance of this model, you'll
         return(f"{self.first_name} {self.last_name}") # get a string like "John Doe" if first_name is "John" and last_name is "Do
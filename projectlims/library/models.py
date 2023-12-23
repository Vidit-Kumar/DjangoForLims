from django.db import models

# Run a command to actually create the table in the database.
# >py manage.py makemigrations library  (Django creates a file describing the changes and stores the file in the /migrations/ folder)
# >py manage.py migrate (this create table by executing sql command)
# Check sql using this command >py manage.py sqlmigrate library 0001
# Create your models here.
class Library(models.Model):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    page_count = models.IntegerField()
    category = models.CharField(max_length=50)
    shelf_location = models.CharField(max_length=50)
    published_date = models.DateField()
    is_in_stock = models.BooleanField(default=True)
    date_checked_out = models.DateField(null=True, blank=True)

  



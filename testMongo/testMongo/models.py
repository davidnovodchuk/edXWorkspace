from django.db import models
  
class School(models.Model):
    name = models.TextField()
    address = models.TextField()

    class MongoMeta:
        db_table = 'Schools'
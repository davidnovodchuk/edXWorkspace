from django.db import models
  
class School(models.Model):
    name = models.TextField()
    address = models.TextField()

    class MongoMeta:
        db_table = 'Schools'

class File(models.Model):
    name = models.TextField()
    data = models.TextField()

    class MongoMeta:
        db_table = 'Files'

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
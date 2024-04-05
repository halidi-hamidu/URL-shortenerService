from django.db import models
import uuid
# class OriginalURL(models.Model):
    #   id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     url = models.CharField(max_length=200)   

#     def __str__(self):
#         return self.url

# class ShortenedURL(models.Model):
    # id = models.UUIDField(
        # primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     original_url = models.OneToOneField(OriginalURL, on_delete=models.CASCADE)
#     shortened_url = models.CharField(max_length=100)   

#     def __str__(self):
#         return self.shortened_url


# start: UrlModel

class UrlModels(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    original_url = models.CharField(max_length=1000)   
    shortened_url = models.CharField(max_length=500) 

    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Url Shortened Service Table"

    def __str__(self):
        return str(self.original_url)

# end:UrlModel

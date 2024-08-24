from django.db import models

# Create your models here.

class University(models.Model):
    id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=100)
    api_url = models.URLField()
    name_field = models.CharField(max_length=100)
    email_field = models.CharField(max_length=100, blank=True, null=True)
    phone_field = models.CharField(max_length=15, blank=True, null=True)
    country_field = models.CharField(max_length=100, blank=True, null=True)
    state_field = models.CharField(max_length=100, blank=True, null=True)
    city_field = models.CharField(max_length=100, blank=True, null=True)
    district_field = models.CharField(max_length=100, blank=True, null=True)
    program_field = models.CharField(max_length=100, blank=True, null=True)
    course_field = models.CharField(max_length=100, blank=True, null=True)
    source_field = models.CharField(max_length=100, blank=True, null=True)
    extra_field = models.JSONField(blank=True, null=True)
    wrap_in_array = models.BooleanField(default=False)

    def __str__(self):
        return self.university_name

class Lead(models.Model):
    id = models.AutoField(primary_key=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null= True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    program = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    extra = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

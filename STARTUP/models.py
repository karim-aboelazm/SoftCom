from django.db import models

class Company(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    country     = models.CharField(max_length=100)
    privacy     = models.CharField(max_length=100)
    city        = models.CharField(max_length=100)
    phone_No    = models.CharField(max_length=15)
    email       = models.EmailField()
    fb_link     = models.URLField(blank=True)
    tw_link     = models.URLField(blank=True)
    ln_link     = models.URLField(blank=True)
    def __str__(self):
        return self.title.upper()

class Job_Categories(models.Model):
    category    = models.CharField(max_length=200)
    def __str__(self):
        return self.category.capitalize()

class Jobs(models.Model):
    category    = models.ForeignKey(Job_Categories,on_delete=models.CASCADE)
    title       = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title.capitalize()

class Services(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField()
    image       = models.ImageField(upload_to='services/')
    def __str__(self):
        return self.title.capitalize()

class Projects_had_done(models.Model):
    category    = models.ForeignKey(Job_Categories,on_delete=models.CASCADE)
    title       = models.CharField(max_length=255)
    details     = models.TextField()
    image       = models.ImageField(upload_to='pro_had_finished/')
    def __str__(self):
        return self.title.capitalize()

class Projects_had_not_done(models.Model):
    category    = models.ForeignKey(Job_Categories,on_delete=models.CASCADE)
    title       = models.CharField(max_length=255)
    details     = models.TextField()
    image       = models.ImageField(upload_to='pro_had_not_finished/')
    def __str__(self):
        return self.title.capitalize()

class OurTeam(models.Model):
    name  = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    job   = models.CharField(max_length=255)
    def __str__(self):
        return self.name.capitalize()
        
class Testimonial(models.Model):
    name  = models.CharField(max_length=255)
    address = models.CharField(max_length=400)
    image = models.ImageField(upload_to='testimonial/') 
    letter = models.TextField()
    def __str__(self):
        return self.name.capitalize()

class OurStatistics(models.Model):
    project_done_no       = models.IntegerField(default=0)
    users_world_no        = models.IntegerField(default=0)
    avilable_countries_no = models.IntegerField(default=0)
    award_winners_no      = models.IntegerField(default=0)
    
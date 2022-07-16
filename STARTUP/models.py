from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator

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
    define_video= models.FileField(upload_to='videos/', blank=True ,null=True,
                                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    
    def save(self, *args, **kwargs):
        if Company.objects.count() == 1:
            return 
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

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
    slug        = models.SlugField(null=True,blank=True)
    client      = models.CharField(max_length=225)
    start_date  = models.DateTimeField(null=True, blank=True)
    end_date    = models.DateTimeField(null=True, blank=True)
    project_url = models.URLField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Projects_had_done, self).save(*args, **kwargs)
    def __str__(self):
        return self.title.capitalize()

class Projects_had_not_done(models.Model):
    category    = models.ForeignKey(Job_Categories,on_delete=models.CASCADE)
    title       = models.CharField(max_length=255)
    details     = models.TextField()
    image       = models.ImageField(upload_to='pro_had_not_finished/')
    slug        = models.SlugField(null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Projects_had_not_done, self).save(*args, **kwargs)
    
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
    def save(self, *args, **kwargs):
        if OurStatistics.objects.count() == 1:
            return 
        super(OurStatistics, self).save(*args, **kwargs)

    def __str__(self):
        return "Current Statistics"

class Reward(models.Model):
    image    = models.ImageField(upload_to='reward/')
    def __str__(self):
        return "Reward - "+ str(self.id)
    
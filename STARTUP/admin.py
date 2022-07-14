from django.contrib import admin
from .models import *

tables = [Company,Job_Categories,
          Jobs,Services,Projects_had_done,
          Projects_had_not_done,OurTeam,
          Testimonial,OurStatistics]

for table in tables:
    admin.site.register(table)
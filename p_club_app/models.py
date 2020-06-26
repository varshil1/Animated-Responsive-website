from django.db import models
from django.utils import timezone
# Create your models here.
import os
from datetime import datetime
from datetime import date

class Home_about_us(models.Model):
    #Table to store data about the about us field and contact us field of home page
    id=models.AutoField(primary_key=True)
    about_us=models.CharField(max_length=2000,null=False) #description of about us on home page
    contact_us=models.CharField(max_length=200,null=False) #description of contact us on home page
    
    def __str__(self):
        return str(self.id)

class Home_desc(models.Model):
    #Table to store data about the heading field and image field of home page carousel
    id=models.AutoField(primary_key=True)
    head_1=models.CharField(max_length=50,null=False)
    head_2=models.CharField(max_length=50,null=False)
    img1= models.ImageField(upload_to='home_car',default=True)
    img2= models.ImageField(upload_to='home_car',default=True)
    img3= models.ImageField(upload_to='home_car',default=True)

    def __str__(self):
        return str(self.id)
    
pref={("High","High"),
    ("Low","Low")}
    #A set of tuples for choice to give preference to events by admin to display on home page
class Events(models.Model):
    #Table Of storing details of events
    event_id = models.AutoField(primary_key=True) #event id
    event_name = models.CharField(max_length=256) 
    event_type = models.CharField(max_length=256) 
    event_date = models.DateTimeField(default=timezone.now)
    event_desc = models.CharField(max_length=400,null=False) #description of events
    reg_link = models.URLField(null=False) #registration link
    event_poster = models.ImageField(upload_to='event',default=True)
    event_pref=models.CharField(max_length=10,choices=pref,default='Low') # give preference to display on home page
    #give high preference to display on home screen
    def __str__(self):
        return str(self.event_name)
    def hour(self):
        return str(self.event_date.hour)
    def minute(self):
        return str(self.event_date.minute)
    def second(self):
        return str(self.event_name.second)
    def is_past(self):
        #method to find whether event is from past or not
        ev_month=int(self.event_date.month)
        today_month=int(datetime.now().strftime("%m"))
        
        ev_day=int(self.event_date.day)
        today_day=int(datetime.now().strftime("%d"))
        
        ev_year=int(self.event_date.year)
        today_year=int(datetime.now().strftime("%Y"))
        today_hour=int(datetime.now().strftime("%H"))
        today_minute=int(datetime.now().strftime("%M"))
        today_second=int(datetime.now().strftime("%S"))
        
        d1=datetime(ev_year,ev_month,ev_day,self.event_date.hour,self.event_date.minute,self.event_date.second)
        d2=datetime(today_year,today_month,today_day,today_hour,today_minute,today_second)
        # print(d2>d1)
        return d2>d1
        
    def is_present(self):
        #method to find whether event is today or not
        ev_month=int(self.event_date.month)
        today_month=int(datetime.now().strftime("%m"))
        
        ev_day=int(self.event_date.day)
        today_day=int(datetime.now().strftime("%d"))
        
        ev_year=int(self.event_date.year)
        today_year=int(datetime.now().strftime("%Y"))
        
        today_hour=int(datetime.now().strftime("%H"))
        today_minute=int(datetime.now().strftime("%M"))
        today_second=int(datetime.now().strftime("%S"))
        
        d1=date(ev_year,ev_month,ev_day)
        d2=date(today_year,today_month,today_day)
        
        d3=datetime(ev_year,ev_month,ev_day,self.event_date.hour,self.event_date.minute,self.event_date.second)
        d4=datetime(today_year,today_month,today_day,today_hour,today_minute,today_second)
        
        # print(d2==d1 and d3>d4)
        return d2==d1 and d3>d4


    def is_future(self):
        #method to find whether event is future
        ev_month=int(self.event_date.month)
        today_month=int(datetime.now().strftime("%m"))
        
        ev_day=int(self.event_date.day)
        today_day=int(datetime.now().strftime("%d"))
        
        ev_year=int(self.event_date.year)
        today_year=int(datetime.now().strftime("%Y"))
        
        d1=date(ev_year,ev_month,ev_day)
        d2=date(today_year,today_month,today_day)
        
        # print(d2<d1)
        return d2<d1
        # return datetime.now().strftime("%B %d %Y")>self.event_date

class Login(models.Model):
    # Table for login field
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return str(self.name)

class Resources(models.Model):
    # Table for resource field
    resource_id = models.AutoField(primary_key=True)
    resource_name = models.CharField(max_length=256)
    resource_desc = models.CharField(max_length=300,default=True)
    res_link = models.URLField(null=True)
    resource_img = models.ImageField(default=True)

    def __str__(self):
        return str(self.resource_name)


class Timeline(models.Model):
    img_date = models.DateTimeField()
    img_src = models.ImageField(default=True)

    def __str__(self):
        return str(self.img_date)

class About_us(models.Model):
    # Table to store data for about us page
    desc = models.CharField(max_length=2000)# description Make TextField
    objectives = models.CharField(max_length=2000) # objectives
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.desc)

class Team(models.Model):
    # Table to store data of team members
    name=models.CharField(max_length=100,unique=True)
    position=models.CharField(max_length=100)
    team_id = models.AutoField(primary_key=True)
    position_order=models.IntegerField(default=True,editable=False)
    images=models.ImageField(upload_to='profile_image',blank=True)

    
    def save(self, *args, **kwargs):
        if(self.position=="secretary" or self.position=="Secretary"):
            self.position_order=1
        elif(self.position=="Joint Secretary" or self.position=="joint Secretary" or self.position=="joint secretary"):
            self.position_order=2
        elif(self.position=="Treasurer" or self.position=="treasurer"):
            self.position_order=3
        elif(self.position=="Student Mentor" or self.position=="Student mentor" or self.position=="student mentor"):
            self.position_order=4
        elif(self.position=="Social Media handler"):
            self.position_order=5
        elif(self.position=="Content writer" or self.position=="Content Writer" or self.position=="content writer"):
            self.position_order=6
        else:
            self.position_order=7
        # self.image='Hey.png'
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # do_something_else()
        # t=Team.objects.get(name=self.name)
        
        

    def __str__(self):
        return str(self.name)
    
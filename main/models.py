from django.db import models


class InfoModel(models.Model):
    # EMERGANCY
    emergency_number = models.IntegerField
    contact_number = models.IntegerField

    # Logo model
    logo = models.ImageField(upload_to='logo/')

    # WORKING HOURS
    working_days = models.CharField(max_length=255)
    working_time = models.CharField(max_length=255)
    weekend_days = models.CharField(max_length=255, null=True, blank=True)
    weekend_time = models.CharField(max_length=255, null=True, blank=True)

    # Locations
    location = models.CharField(max_length=300)
    address = models.CharField(max_length=255)

    # Links 
    telegram_link=models.CharField(max_length=300)
    instagram_link=models.CharField(max_length=300)
    email = models.EmailField()


# Our Services Model
# class OurServicesModel(models.Model):
#     img = models.ImageField(upload_to='services/')
#     services_title = models.CharField(max_length=255)
#     services_text = models.TextField(blank=True,null=True)

#     def __str__(self):
#         return self.services_title


        
# About Us ichidegi FAQning tepasidegi Block

# class AboutusblockModel(models.Model):
#     block_img = models.ImageField(upload_to='aboutus_blog/')
#     block_title = models.CharField(max_length=255)
#     block_text = models.TextField()

#     def __str__(self):
#         return self.block_title

# Doctors Model
class Doctors(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Doktorlar'

    def __str__(self):
        return self.name + ' ' + self.specialty


#  Operation Attented Model
class Operationg_Attented(models.Model):
    img = models.ImageField(upload_to='operation/img/')
    video = models.FileField(upload_to='operation/vid/')
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    project_detail = models.TextField()
    project_detail_img = models.ImageField(upload_to='operation/img/', null=True, blank=True)
    video_under_text = models.TextField()
    participating_doctors = models.ManyToManyField(Doctors)

    def __str__(self):
        return self.title

# Doctors detail Model
class Doctors_about(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    biography = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    awards = models.TextField(null=True, blank=True)
    operations = models.ManyToManyField(Operationg_Attented)

    def __str__(self):
        return self.doctor.name

# FAQ Model
class FAQ(models.Model):
    CHOICE = (
        (1, 'About'),
        (2, 'Service'),
        (3, 'Doctor'),
    )
    status = models.SmallIntegerField(choices=CHOICE)
    savol = models.CharField(max_length=255)
    javob = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return self.get_status_display()


# Testimonials Model
class Testimonials(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=40)

    def __str__(self):
        return self.text

# Blog Model
class Blog(models.Model):
    img = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Bloglar'

    def __str__(self):
        return self.title

# News Model
class News(models.Model):
    CHOICE = (
        (1, 'Top'),
        (2, 'Normal')
    )
    status = models.SmallIntegerField(choices=CHOICE)
    img = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Yangiliklar'

    def __str__(self):
        return self.title

# Our Service
class OurService(models.Model):
    img = models.ImageField(upload_to='service/')
    banner_img = models.ImageField(upload_to='service/')
    small_title = models.CharField(max_length=255)
    large_title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    large_text = models.TextField()
    banner = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Servislar'

    def __str__(self):
        return self.small_title


class Introduction(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='introduction/vid/')
    large_text = models.TextField()
    small_text = models.TextField()

    class Meta:
        verbose_name_plural = 'Introduction'

    def __str__(self):
        return self.title


class Consulting(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    department = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctors, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    number = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.department + ' ' + self.name


class Aboutus_block(models.Model):
    img = models.ImageField(upload_to='about_us_blog/')
    title = models.CharField(max_length=255)
    large_text = models.TextField()
    small_text = models.TextField()

    
    


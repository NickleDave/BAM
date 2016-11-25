from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class volunteer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    UNDERGRAD = 'UG'
    GRAD_STUDENT = 'GR'
    POSTDOC = 'PD'
    PROF = 'PR'
    OTHER = 'OT'
    POSITION_CHOICES = (
        (UNDERGRAD, 'Undergraduate'),
        (GRAD_STUDENT, 'Graduate student'),
        (POSTDOC, 'Post-doctoral'),
        (PROF, 'Professor'),
        (OTHER, 'Other'),
        )
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
        default=GRAD_STUDENT,
        )
    email = models.EmailField()
    phone = PhoneNumberField()

    EMORY = 'EM'
    GTECH = 'GT'
    GSU = 'GS'
    UNIV_CHOICES = (
        (EMORY, 'Emory University'),
        (GTECH, 'Georgia Tech'),
        (GSU, 'Georgia State University'),
        )    
    university = models.CharField(
        max_length=2,
        choices=UNIV_CHOICES)

    MON = 'MO'
    TUE = 'TU'
    WED = 'WE'
    THU = 'TH'
    FRI = 'FR'
    SAT = 'SA'
    SUN = 'SU'
    DAY_CHOICES = (
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday'),
        )
     
    weekdays_available = models.CharField(
        max_length = 2,
        choices = DAY_CHOICES)
        
    more_than_one_visit = models.BooleanField()

    KINDERGARTEN = 'KI'
    PRIMARY = 'PR'
    MIDDLE = 'MI'
    SECONDARY = 'SE'
    GRADE_CHOICES = (
        (KINDERGARTEN, 'K'),
        (PRIMARY, '1st-5th'),
        (MIDDLE, '6th-8th'),
        (SECONDARY, '9th-12th'),s
        ) 
    grade_preference = models.CharField(
        max_length = 2,
        choices = GRADE_CHOICES)

    HALF = 'HA'
    ONE = 'ON'
    ONEHALF = 'OH'
    DRIVE_TIME_CHOICES = (
        (HALF, 'Half an hour or less'),
        (ONE, 'One hour or less'),
        (ONEHALF, 'One and a half hours or less'),
        )
    driving_time = models.CharField(
        max_length = 2,
        choices = DRIVE_TIME_CHOICES)
    notes = models.TextField()

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=250)
    school_address = models.CharField(max_length=300)
    school_district = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()
    preferred_method_of_contact = models.CharField(
        max_length = 2
        choices = (('PH', 'Phone'),('EM', 'e-mail'),)
        )

    GRADE_LEVEL_CHOICES = (
        ('KI', 'Kindergarten'),
        ('FI', 'First'),
        ('SE', 'Second'),
        ('TH', 'Third'),
        ('FO', 'Fourth'),
        ('FI', 'Fifth'),
        ('SI', 'Sixth'),
        ('SE', 'Seventh'),
        ('EI', 'Eighth'),
        ('NI', 'Ninth'),
        ('TE', 'Tenth'),
        ('EL', 'Eleventh'),
        ('TW', 'Twelfth'),
        )
    grade_level = models.Charfield(
        max_length = 2,
        choices = GRADE_LEVEL_CHOICES
        )
    number_of_classes = models.PositiveIntegerField(default=1)
    students_per_class = models.PositiveIntegerField()
    number_of_hours_requested = models.DecimalField(max_digits=4,decimal_places=2)
    MONTH_CHOICES = (
        ('JA', 'January'),
        ('FE', 'February'),
        ('MA', 'March'),
        ('AP', 'April'),
        ('MY', 'May'),
        ('JU', 'June'),
        ('JL', 'July',),
        ('AU', 'August'),
        ('SE', 'September'),
        ('OC', 'October'),
        ('NO', 'November'),
        ('DE', 'December'),
        )
    available_months_for_visit = models.CharField(
        max_length = 2,
        choices = MONTH_CHOICES
        )
    possible_times_for_visit = models.CharField(max_length = 300)
    questions_or_comments = models.TextField()
    notes = models.TextField()

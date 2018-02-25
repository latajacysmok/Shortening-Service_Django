from django.db import models
from .utils import code_generator, create_shortcode
from .validators import validate_dot_com, validate_url

class KirrUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrUrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=False)
        return qs
    def refresh_shortcodes(self, items = 100):
        qs = KirrUrl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {}".format(new_codes)

class KirrUrl(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=128, unique=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    objects = KirrUrlManager()
    some_random = KirrUrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
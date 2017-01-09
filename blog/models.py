from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Category(models.Model):
    FITNESS = 'F'
    NUTRITION = 'N'
    LIFESTYLE = 'L'
    PRODUCTIVITY = 'P'
    ENTREPRENEURSHIP = 'E'
    CATEGORY_CHOICES = (
        (FITNESS, 'Fitness'),
        (NUTRITION, 'Nutrition'),
        (LIFESTYLE, 'Lifestyle'),
        (PRODUCTIVITY, 'Productivity'),
        (ENTREPRENEURSHIP, 'Entrepreneurship'),
    )

    name = models.CharField(choices=CATEGORY_CHOICES, blank=False, max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(default='', editable=False )


    @models.permalink
    def get_absolute_url(self):
        kwargs = {'year': self.created_at.year,
              'month': self.created_at.month,
              'day': self.created_at.day,
              'slug': self.slug,
              'pk': self.pk}
        return reverse('post_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.

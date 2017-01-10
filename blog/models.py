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
    slug = models.SlugField(default='', editable=False, unique=True, max_length=140)

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {
            'slug': self.slug,
            'pk': self.pk,
        })

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

# Create your models here.

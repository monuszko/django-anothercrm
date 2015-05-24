from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    mission = models.TextField(blank=True, default="To make money.")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        #TODO: ask on IRC about these imports
        from django.core.urlresolvers import reverse
        from django.utils.text import slugify
        slug = slugify(self.name)
        return reverse(
                'anothercrm:company', kwargs={'name': slug, 'pk': self.id})

    def employees_by_position(self):
        return self.employee_set.all().order_by('position')

    class Meta:
        verbose_name_plural = 'companies'


SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )

class Employee(models.Model):
    #TODO: validators for name
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    company = models.ForeignKey(Company)
    position = models.CharField(max_length=100)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        from django.utils.text import slugify
        fname = slugify(self.firstname)
        lname = slugify(self.lastname)
        kwargs = {
                'firstname': fname,
                'lastname': lname,
                'pk': self.id,
                }
        return reverse('anothercrm:employee', kwargs=kwargs)

    def __unicode__(self):
        return u'{0} {1} - {2} at {3}'.format(
                self.firstname, self.lastname, self.position, self.company)

    


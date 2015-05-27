from django.db import models


class Person(models.Model):
    SEX_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            )
    #TODO: validators for name
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

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
        return reverse('anothercrm:person', kwargs=kwargs)

    def __unicode__(self):
        return u'{0} {1}'.format(self.firstname, self.lastname)

    def employee_count(self):
        '''
        Returns the number of relationships where the person
        is employed at a company.
        '''
        return self.relationship_set.filter(relatype__category='E').count()

    def client_count(self):
        '''
        Returns the number of relationships where the person
        is a cliento of a company.
        '''
        return self.relationship_set.filter(relatype__category='C').count()

    def company_names(self):
        '''
        Returns the names of companies the person is involved with.
        '''
        return ', '.join(self.relationship_set.all().values_list(
                                                   'company__name', flat=True))

    def employee_relationships(self):
        '''
        Returns the number of relationships where the person
        is employed at a company.
        '''
        return self.relationship_set.filter(relatype__category='E')

    def client_relationships(self):
        '''
        Returns the number of relationships where the person
        is a cliento of a company.
        '''
        return self.relationship_set.filter(relatype__category='C')


class Company(models.Model):
    name = models.CharField(max_length=100)
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
        '''
        Returns Relations with employees - not Persons.
        '''
        return self.relationship_set.filter(
                             relatype__category='E').order_by('relatype__name')

    def clients_by_type(self):
        '''
        Returns Relations with clients, agents etc - not Persons.
        '''
        return self.relationship_set.filter(
                             relatype__category='C').order_by('relatype__name')

    class Meta:
        verbose_name_plural = 'companies'


class RelationshipType(models.Model):
    CATEGORY_CHOICES = (
            ('E', 'Employee'),
            ('C', 'Client'),
            )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.name, self.get_category_display())


class Relationship(models.Model):
    relatype = models.ForeignKey(RelationshipType, verbose_name='relationship type')
    company = models.ForeignKey(Company)
    person = models.ForeignKey(Person)

    def __unicode__(self):
        return u'{0} {1} {2} {3}'.format(self.person.firstname,
                             self.person.lastname, self.relatype, self.company)


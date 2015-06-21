from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    SEX_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            )
    #TODO: validators for name, mobile...
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    email = models.EmailField(
                   max_length=200, verbose_name=_('Email address'), blank=True)
    mobile = models.CharField(
              max_length=20, verbose_name=_('Mobile Phone Number'), blank=True)

    address = models.CharField(max_length=100, verbose_name=_('Address'),
                                help_text=_('24 Badger Rd., etc.'), blank=True)
    zipcode = models.CharField(max_length=10, verbose_name=_('Postal code'),
                    help_text=_("For example, '80-209' in Poland"), blank=True)
    city = models.CharField(max_length=100, verbose_name=_('City'), blank=True)
    state = models.CharField(
                           max_length=100, verbose_name=_('State'), blank=True)
    country = models.CharField(
                           max_length=2, verbose_name=_('Country'), blank=True)

    creation_date = models.DateTimeField(
                            verbose_name=_('Creation Date'), auto_now_add=True)
    modification_date = models.DateTimeField(
                            verbose_name=_('Modification Date'), auto_now=True)

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


class Trade(models.Model):
    name = models.CharField(max_length=100, unique=True,
                                   help_text="the industry the company is in.")

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    mission = models.TextField(blank=True, default="To make money.")
    trades = models.ManyToManyField(Trade, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        #TODO: ask on IRC about these imports
        from django.core.urlresolvers import reverse
        from django.utils.text import slugify
        slug = slugify(self.name)
        return reverse(
                'anothercrm:company', kwargs={'name': slug, 'pk': self.id})

    def get_trades(self):
        return ', '.join(tr.name for tr in self.trades.all())
    get_trades.short_description='Trade(s)'
    get_trades.admin_order_field='trades'

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
        verbose_name_plural = _('companies')


class RelationshipType(models.Model):
    CATEGORY_CHOICES = (
            ('E', 'Employee'),
            ('C', 'Client'),
            )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50, unique=True,
            help_text=("For employees, this is position. For customers, it can"
                       " be 'regular customer', etc."))
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.name, self.get_category_display())


class Relationship(models.Model):
    relatype = models.ForeignKey(RelationshipType,
            verbose_name=_('relationship type'))
    company = models.ForeignKey(Company)
    person = models.ForeignKey(Person)

    def __unicode__(self):
        return u'{0} {1} {2} {3}'.format(self.person.firstname,
                             self.person.lastname, self.relatype, self.company)


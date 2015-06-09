# -*- coding: utf-8
import os, sys

proj_path = "/home/b0rsuk/warsztat/projekty/django-anothercrm"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


import factory
from itertools import groupby
from operator import itemgetter

# PEP 3208
from anothercrm.models import (Company,
        Person, Relationship, RelationshipType, Trade)


class TradeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Trade
        django_get_or_create = ('name',)


TradeFactory(name='combat supplier')
TradeFactory(name='exotic goods')
TradeFactory(name='bulk goods')
TradeFactory(name='slave trader')


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company
        django_get_or_create = ('name',)

    @factory.post_generation
    def trades(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for trade in extracted:
                self.trades.add(trade)


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person
        django_get_or_create = ('firstname', 'lastname', 'sex')


class RelationshipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Relationship
        django_get_or_create = ('relatype', 'company', 'person')


class RelationshipTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RelationshipType
        django_get_or_create = ('category', 'name')


people = (
        (u'Markus', u'Keuneke', 'M'),
        (u'Cato', u'Noess', 'F'),
        (u'Mie', u'Aldemar', 'F'),
        (u'Geir', u'Johannesen', 'F'),
        (u'Jonathan', u'Craig', 'M'),
        (u'Feeb', u'Dafo', 'F'),
        (u'Harvey', u'Hansen', 'M'),
        (u'Kael', u'King', 'M'),
        (u'Kelly', u'Hrdina', 'F'),
        (u'Marle', u'Davia', 'F'),
        (u'Catherine', u'Coleman', 'F'),
        (u'Pyrrha', u'Trovatelli', 'F'),
        (u'Chaz', u'Serir', 'M'),
        (u'Valentina', u'McCall', 'F'),
        (u'Ryan', u'Jung', 'M'),
        (u'Nelson', u'Ramos', 'M'),
        (u'Hugh', u'Jack', 'M'),
        (u'Paola', u'Riggs', 'F'),
        (u'Rajel', u'Valjurai', 'F'),
        (u'William', u'Gregory-Heap', 'M'),
        (u'Verena', u'Syburg', 'F'),
        (u'Takuya', u'Roberson', 'M'),
        (u'Nicholas', u'Porsonby', 'M'),
        (u'André', u'Marx', 'M'),
        (u'Mariana', u'C da Silva', 'F'),
        (u"Loc'eed", 'Ironheart', 'M'),
        (u'Panzerella', u'Winterbourne', 'F'),
        (u'Aleksi', u'Rönkkö', 'M'),
        (u'Ernest', u'Szoka', 'M'),
        (u'Beatriz', u'Randall', 'F'),
        (u'Matis', u'Saro', 'M'),
        (u'Lucya', u'Rosario', 'F'),
        (u'Anthal', u'Kyten', 'F'),
        (u'Hiroto', u'Guzman', 'M'),
        (u'Robert', u'Long', 'M'),
        (u'Erin', u"O'Connell", 'F'),
        (u'Thomas', u'Trucker', 'M'),
        (u'Steven', u'Wilcox', 'M'),
        (u'Lorenzo', u'Jennings', 'M'),
        (u'Hayden', u'Simons', 'M'),
        (u'Phil', u'Costa', 'M'),
        (u'Jacob', u'Sennett', 'M'),
        (u'Theodore', u'Seraphimus', 'M'),
        (u'Buffy', u'Hoffman', 'F'),
        (u'Christine', u'Yates', 'F'),
        (u'Polo', u'Larson', 'M'),
        (u'Genevieve', u'Cwiklik', 'F'),
        (u'Jason', u'Roland', 'M'),
        (u'Patrick', u'Misale', 'M'),
        (u'Jorge', u'Paredes', 'M'),
        (u'Humberto', u'Roca', 'M'),
        (u'Ida', u'Barber', 'F'),
        (u'Eita', u'Anderson', 'F'),
        (u'Callie', u'Shelton', 'F'),
        (u'Soder', u'Berg', 'F'),
        (u'Luro', u'Hilaire', 'M'),
        (u'Artyom', u'Lyons', 'M'),
        (u'Rae', u'Meadows', 'F'),
        (u'Minyoung', u'Kim', 'F'),
        (u'Maria', u'Campos', 'F'),
        (u'Violet', u'Ramsey', 'F'),
        (u'Katia', u'Mack', 'F'),
        (u'Branden', u'Dupuis', 'F'),
        (u'Daichi', u'Evans', 'M'),
        (u'Norma', u'Valdez', 'F'),
        (u'Alfred', u'Clark', 'M'),
        (u'Garen', u'Fielder', 'M'),
        (u'Alexis', u'Duncan', 'F'),
        (u'Rene', u'Krause', 'M'),
        (u'Yakov', u'Robinson', 'M'),
        (u'Amy', u'Roper', 'F'),
        (u'Brandon', u'Wingfield', 'M'),
        (u'Joe', u'Rediger', 'M'),
        (u'Lawrence', u'Lavigne', 'M'),
        (u'Yolanda', u'Mahasen', 'F'),
        (u'Jova', u'Thornton', 'F'),
        (u'Gary', u'Wooldridge', 'F'),
        (u'Jackson', u'Hightower', 'M'),
        (u'Mathew', u'Cormier', 'M'),
        (u'Vaska', u'Neemor', 'F'),
        (u'Sten', u'Hansen', 'M'),
        )


for p in people:
    PersonFactory(firstname=p[0], lastname=p[1], sex=p[2])


#these were used to generate letter sets for employees/customers
#
#firstname_last_letters = sorted([p[0][-1].lower() for p in people])
#lastname_last_letters = sorted([p[1][-1].lower() for p in people])
#lastname_last_letters = [l for l in lastname_last_letters if l.isalpha()]
#firsts = {a: len(list(b)) for a, b in groupby(firstname_last_letters)}
#seconds = {a: len(list(b)) for a, b in groupby(lastname_last_letters)}


companies = (
        ('Industrial Lubricants', []),
        ('Linstorm Incorporated', ['slave trader']),
        ('Lumen Travelers', ['exotic goods']),
        ('Wulan Import Company', ['bulk goods']),
        ('Kayulu Consortium', ['combat supplier', 'slave trader']),
        ('Tukus Securities', ['combat supplier']),
        ('Lartmech Interstellar', ['exotic goods']),
        ('Cheevor Partners', ['bulk goods']),
        ('Zephor Industries', ['combat suppler', 'bulk goods']),
        )


for c in companies:
    trades = Trade.objects.filter(name__in=c[1])
    CompanyFactory(name=c[0], trades=trades)


rtypes = (
       ('C', 'normal customer'),
       ('C', 'bad customer'),
       ('C', 'regular customer'),
       ('E', 'marketing'),
       ('E', 'sales'),
       ('E', 'technical'),
        )


for rt in rtypes:
    RelationshipTypeFactory(category=rt[0], name=rt[1])


relationships = (
    ('Industrial Lubricants', 'normal customer', 'e'),
    ('Industrial Lubricants', 'regular customer', 'b'),
    ('Industrial Lubricants', 'bad customer', 's'),
    ('Industrial Lubricants', 'sales', 'l'),
    ('Industrial Lubricants', 'marketing', 'e'),
    ('Industrial Lubricants', 'technical', '-'),
    ('Linstorm Incorporated', 'normal customer', 'b'),
    ('Linstorm Incorporated', 'regular customer', 'o'),
    ('Linstorm Incorporated', 'bad customer', 'k'),
    ('Linstorm Incorporated', 'sales', 'm'),
    ('Linstorm Incorporated', 'marketing', '-'),
    ('Linstorm Incorporated', 'technical', 'x'),
    ('Lumen Travelers', 'normal customer', 'l'),
    ('Lumen Travelers', 'regular customer', 'h'),
    ('Lumen Travelers', 'bad customer', 'a'),
    ('Lumen Travelers', 'sales', '-'),
    ('Lumen Travelers', 'marketing', 'a'),
    ('Lumen Travelers', 'technical', 'm'),
    ('Wulan Import Company', 'normal customer', 'w'),
    ('Wulan Import Company', 'regular customer', '-'),
    ('Wulan Import Company', 'bad customer', 'a'),
    ('Wulan Import Company', 'sales', 's'),
    ('Wulan Import Company', 'marketing', '-'),
    ('Wulan Import Company', 'technical', '-'),
    ('Kayulu Consortium', 'normal customer', '-'),
    ('Kayulu Consortium', 'regular customer', 'l'),
    ('Kayulu Consortium', 'bad customer', 's'),
    ('Kayulu Consortium', 'sales', '-'),
    ('Kayulu Consortium', 'marketing', 'y'),
    ('Kayulu Consortium', 'technical', '-'),
    ('Tukus Securities', 'normal customer', 'i'),
    ('Tukus Securities', 'regular customer', '-'),
    ('Tukus Securities', 'bad customer', 'h'),
    ('Tukus Securities', 'sales', '-'),
    ('Tukus Securities', 'marketing', '-'),
    ('Tukus Securities', 'technical', 'r'),
    ('Lartmech Interstellar', 'normal customer', 'd'),
    ('Lartmech Interstellar', 'regular customer', '-'),
    ('Lartmech Interstellar', 'bad customer', '-'),
    ('Lartmech Interstellar', 'sales', 'g'),
    ('Lartmech Interstellar', 'marketing', 'z'),
    ('Lartmech Interstellar', 'technical', 'r'),
    ('Cheevor Partners', 'normal customer', '-'),
    ('Cheevor Partners', 'regular customer', 'z'),
    ('Cheevor Partners', 'bad customer', '-'),
    ('Cheevor Partners', 'sales', 'k'),
    ('Cheevor Partners', 'marketing', 'y'),
    ('Cheevor Partners', 'technical', 'e'),
    ('Zephor Industries', 'normal customer', '-'),
    ('Zephor Industries', 'regular customer', '-'),
    ('Zephor Industries', 'bad customer', 'b'),
    ('Zephor Industries', 'sales', 'g'),
    ('Zephor Industries', 'marketing', 'o'),
    ('Zephor Industries', 'technical', 'x'),
        )


for r in relationships:
    last_letter = r[2]
    if last_letter == '-':
        continue
    comp = Company.objects.get(name=r[0])
    rtype = RelationshipType.objects.get(name=r[1])

    if rtype.category == 'C':
        persons = Person.objects.filter(firstname__endswith=last_letter)
    else:
        persons = Person.objects.filter(lastname__endswith=last_letter)
    for pers in persons:
        r = RelationshipFactory(company=comp, relatype=rtype, person=pers)


print('Companies: %s' % Company.objects.all().count())
print('Persons: %s' % Person.objects.all().count())
print('Relationship types: %s' % RelationshipType.objects.all().count())
print('Relationships: %s' % Relationship.objects.all().count())
print('Trades: %s' % Trade.objects.all().count())


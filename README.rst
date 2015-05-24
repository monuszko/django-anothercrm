==========
Anothercrm
==========

Anothercrm is a simple Django app providing CRM functionality.

Quick start
-----------

1. Add "anothercrm" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'anothercrm',
    )

2. Include the anothercrm URLconf in your project urls.py like this::

    url(r'^anothercrm/', include('anothercrm.urls', namespace='anothercrm')),

3. Run `python manage.py migrate` to create the anothercrm models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a privileged user (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/anothercrm/ to access the crm.

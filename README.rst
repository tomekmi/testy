=====
TESTY
=====

Testy is a Web-based multianswer test creator. For each
question, users can choose more than one answer. 
After completing the test, the result is shown and sent
to user e-mail.

Quick start
-----------

1. Add "apptesty" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'apptesty',
    )

2. Include the apptesty URLconf in your project urls.py like this::

    url(r'^testy/', include('polls.urls')),

3. Run `python manage.py migrate` to create the Testy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a test (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/testy/ to participate in the poll. 

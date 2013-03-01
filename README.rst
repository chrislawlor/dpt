{% if False %}

Django 1.5 with Boilerplate and Bootstrap Project Template
==========================================================

About
-----

This django project template uses the following:

* Templates based on HTML5 Boilerplate
* Bootstrap
* LESS
* Sensitive settings loaded from environment variables.
* Separate requirements for local development and production.
* Separate, version-controlled settings for each target environment.
* Django Debug Toolbar and Django Extensions pre-loaded for local development.
* make targets for common development tasks
* Run unit tests with coverage.py for coverage reports
* Automatically builds a README with installation and setup notes.


Getting Started
---------------

* Install Django 1.5
* ``django-admin.py startproject --template https://github.com/chrislawlor/dpt/tarball/master YOURPROJECTNAME``
* Follow instructions below.

{% endif %}

{{ project_name|upper }}
========================

Add a short description of the project here.


Getting Started - Development
-----------------------------

Installing Tools and Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**NOTE** Please follow instructions carefully, as this project has been set up
to avoid some of the common Django anti-patterns that you may be used to. Most
notably, you'll need to define some environment variables.

Set up a virtual environment. Virtualenvwrapper_ is highly recommended.

.. _Virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/

::

    mkvirtualenv {{ project_name }}

The development requirements are defined in the ``requirements`` folder. Note that
these are divided into separate requirements for production and local development.


Install development requirements with::

    pip install -r requirements/local.txt
    
**NOTE:** After the first time installing requirements, be sure to go back and add
version numbers for all the installed libraries. Do *NOT* leave unversioned
items in a requirements file!
    
Install the LESS compiler (requires NodeJS_)

.. _NodeJS: http://nodejs.org/

::

    npm install -g less


Install the ``watchr`` gem::

    gem install watchr
    

Setting Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of keeping sensitive data like the project ``SECRET_KEY`` and
database connection strings in settings files, or worse, keeping them
in an unversioned ``local_settings`` module, we use environment
variables to store these bits of data.

If you're using virtualenvwrapper, a convenient place to define these
is in your ``postactivate`` script. Otherwise, they can go in e.g.
``~/bash_profile``.

You can use a tool like `this secret key generator`_ to generate
a ``SECRET_KEY``.

.. _this secret key generator: http://www.miniwebtool.com/django-secret-key-generator/

**NOTE:** Be sure to keep a backup copy of the ``SECRET_KEY`` used in production!!

Here is a list of the required environment variables:

* {{ project_name|upper }}_DATABASE_NAME

* {{ project_name|upper }}_DATABASE_USER

* {{ project_name|upper }}_DATABASE_PASSWORD

* {{ project_name|upper }}_SECRET_KEY

If you are using virtualenvwrapper, begin editing the ``postactivate`` script as follows::

    cdvirtualenv
    vim bin/postactivate
    
Set the contents as follows::

    #!/bin/bash
    # This hook is run after this virtualenv is activated.
    
    export {{ project_name|upper }}_DATABASE_NAME="prototype";
    export {{ project_name|upper }}_DATABASE_USER="";
    export {{ project_name|upper }}_DATABASE_PASSWORD="";
    export {{ project_name|upper }}_SECRET_KEY="";
    export DJANGO_SETTINGS_MODULE="project.settings.local";

The last line, which sets ``DJANGO_SETTINGS_MODULE`` to ``project.settings.local``,
is not strictly necessary, but helpful to avoid the need for the
``--settings`` flag to django management commands.


Initialize Your Database
~~~~~~~~~~~~~~~~~~~~~~~~

Prototype uses South_ to manage database migrations.

.. _South: http://south.aeracode.org/

::

    make db

**NOTE:** If you've set the ``DJANGO_SETTINGS_MODULE`` environment variable,
you can omit the ``--settings=...`` portion of any ``manage.py`` commands.

Start the Development Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    make server

Now `bask in the glory`_ of all the hard work you didn't have to do to get this far!

.. _bask in the glory: http://localhost:8000/

    
Editing Static Assets
~~~~~~~~~~~~~~~~~~~~~

**TL;DR** Edit LESS source files, compiled to CSS with ``make`` or ``make watch``,
and commit both the LESS source and the compiled CSS.

Static assets are stored in ``static/assets``. We use LESS_, which
must be compiled to CSS. The ``Makefile`` default build target will invoke the
``lessc`` compiler.

.. _LESS: http://lesscss.org/
    
To compile static assets::
    
    make

To avoid having to run ``make`` constantly, running::

    make watch

will automatically run the ``lessc`` compiler when any ``.less`` source
files are changed.

Compiled CSS files must be committed to the repository, since the ``lessc`` compiler
will not be available on production servers.

Running Tests
~~~~~~~~~~~~~

To run project tests and generate a coverage report, run::

    make test

Open ``htmlcov/index.html`` in your browser to view the coverage report.


Deploying
~~~~~~~~~

There is an experimental ``fabfile`` included, which will need to be edited
to fit your needs. Change this documentation as required.












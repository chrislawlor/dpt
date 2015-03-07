{% if False %}

Django 1.7 with Boilerplate and Bootstrap Project Template
==========================================================

About
-----

This django project template uses the following:

* Templates based on HTML5 Boilerplate
* Bootstrap 3.0
* FontAwesome 3.2.1
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

* Install Django 1.7
* ``django-admin.py startproject --template https://github.com/chrislawlor/dpt/zipball/master --extension=py,rst YOURPROJECTNAME``
* Follow instructions below.


Using Bootstrap 2
----------------------------

DPT includes Boostrap 3.0. If you wish to use an older version, download
the desired source from GitHub (probably `Bootstrap 2.3.2`_) and:

.. _Bootstrap 2.3.2: https://github.com/twbs/bootstrap/archive/v2.3.2.zip

* Replace ``static/assets/vendor/bootstrap/less/`` with the ``less`` folder
  from your download.

* Replace ``static/assets/vendor/js/bootstrap.js`` with ``dist/js/bootstrap.js``

* Edit ``static/assets/vendor/bootstrap/less/bootstrap.less``, and replace
  ``@import "sprites.less";`` with ``@import "../../font-awesome/less/font-awesome.less";``

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

The database connection is defined using a URL instead of separate parameters
for database name, password, etc. For PostgreSQL, the string will look like::

    postgresql://username:password@hostname:port/database

For SQLite, use::

    sqlite:////full/path/to/your/database/file.sqlite

You can use a tool like `this secret key generator`_ to generate
a ``SECRET_KEY``.

.. _this secret key generator: http://www.miniwebtool.com/django-secret-key-generator/

**NOTE:** Be sure to keep a backup copy of the ``SECRET_KEY`` used in production!!

Here is a list of the required environment variables:

* {{ project_name|upper }}_DATABASE_URL

* {{ project_name|upper }}_SECRET_KEY

If you are using virtualenvwrapper, begin editing the ``postactivate`` script as follows::

    cdvirtualenv
    vim bin/postactivate
    
Set the contents as follows::

    #!/bin/bash
    # This hook is run after this virtualenv is activated.
    
    export {{ project_name|upper }}_DATABASE_URL="postgresql://username:password@hostname:port/database";
    export {{ project_name|upper }}_SECRET_KEY="";
    export DJANGO_SETTINGS_MODULE="project.settings.local";
    export PYTHONPATH="/path/to/{{ project_name }}/apps";

Setting``DJANGO_SETTINGS_MODULE`` to ``project.settings.local``,
is not strictly necessary, but helpful to avoid the need for the
``--settings`` flag to django management commands.

Similarly, setting ``PYTHONPATH`` lets you use ``django-admin.py`` instead of
``python manage.py``.


Running ``manage.py`` commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Django's ``manage.py`` script is located in the ``apps`` directory. Any
``manage.py`` command can be run as follows::

    python apps/manage.py --settings=project.settings.local COMMAND


**NOTE:** If you've set the ``DJANGO_SETTINGS_MODULE`` environment variable, and
set your ``PYTHONPATH``, you can omit the ``--settings=...`` portion of any 
``manage.py`` commands, and substitute ``django-admin.py`` for ``manage.py``.

For convenience, {{ project_name|capfirst }} provides makefile targets for most
common ``manage.py`` commands. 


Initialize Your Database
~~~~~~~~~~~~~~~~~~~~~~~~

::

    make db


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












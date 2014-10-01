========================
Zinnia-threaded-comments
========================

Zinnia-threaded-comments is a python package providing threaded comments
for `django-blog-zinnia`_ based on `django-contrib-comments`_.

Installation
============

First of all you need to install and configure
`django-app-namespace-template-loader`_ into your project.

Then once `Zinnia is installed`_ on your Django project and this package
installed on your `PYTHON_PATH`, simply register the
``zinnia_threaded_comments`` application in the ``INSTALLED_APP`` section
of your project's settings and then register ``zinnia_threaded_comments``
as the ``COMMENTS_APP``.

Now Zinnia can handle threaded comments.

.. warning::
   `zinnia_threaded_comments` must be registered before the `zinnia` app to bypass
   the loading of the Zinnia's templates.

Protip
======

If you plan to customise the default template of an entry with the
threaded comments, create in your project a ``zinnia/entry_detail.html``
template starting with: ::

  {% extends "zinnia/entry_detail_base.html" %}

By doing this you don't have to reimplement the template logic provided by
the app, and just have to customize the needed blocks.

Going further
=============

More informations about customizations of the comments framework at:
http://django-contrib-comments.readthedocs.org/en/latest/custom.html

.. _`django-blog-zinnia`: http://www.django-blog-zinnia.com/
.. _`django-contrib-comments`: https://github.com/django/django-contrib-comments
.. _`django-app-namespace-template-loader`: https://github.com/Fantomas42/django-app-namespace-template-loader
.. _`Zinnia is installed`: http://docs.django-blog-zinnia.com/en/latest/getting-started/install.html

========================
Zinnia-threaded-comments
========================

Zinnia-threaded-comments is a python package providing threaded comments
for `django-blog-zinnia`_ based on `django.contrib.comments`_.

Installation
============

Once `Zinnia is installed`_ on your Django project and this package installed
on your `PYTHON_PATH`, simply register the ``zinnia_threaded_comments``
application in the ``INSTALLED_APP`` section of your project's settings and
then register ``zinnia_threaded_comments`` as the ``COMMENTS_APP``.

Now Zinnia can handle threaded comments.

.. warning::
   * `zinnia_threaded_comments` must be registered before the `zinnia` app to bypass
     the loading of the Zinnia's templates.
   * You need to use the ``django.template.loaders.eggs.Loader`` template
     loader if you have installed the package as an egg.

More informations about customizations of the comments framework at:
https://docs.djangoproject.com/en/dev/ref/contrib/comments/custom/

.. _`django-blog-zinnia`: http://www.django-blog-zinnia.com/
.. _`django.contrib.comments`: https://docs.djangoproject.com/en/dev/ref/contrib/comments/
.. _`Zinnia is installed`: http://docs.django-blog-zinnia.com/en/latest/getting-started/install.html

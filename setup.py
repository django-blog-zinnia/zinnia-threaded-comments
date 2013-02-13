"""Setup script for zinnia-threaded-comments"""
from setuptools import setup
from setuptools import find_packages

import zinnia_threaded_comments

setup(
    name='zinnia-threaded-comments',
    version=zinnia_threaded_comments.__version__,

    description='Threaded comments for django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, blog, weblog, zinnia, comments, threaded',

    author=zinnia_threaded_comments.__author__,
    author_email=zinnia_threaded_comments.__email__,
    url=zinnia_threaded_comments.__url__,

    packages=find_packages(exclude=['demo_zinnia_threaded_comments']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_threaded_comments.__license__,
    include_package_data=True,
    zip_safe=False
)

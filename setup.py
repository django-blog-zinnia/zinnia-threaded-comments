"""Setup script for zinnia-threaded-comments"""
from setuptools import setup
from setuptools import find_packages

__version__ = '0.2'
__license__ = 'BSD License'

__author__ = 'Fantomas42'
__email__ = 'fantomas42@gmail.com'

__url__ = 'https://github.com/Fantomas42/zinnia-threaded-comments'

setup(
    name='zinnia-threaded-comments',
    version=__version__,

    description='Threaded comments for django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, blog, weblog, zinnia, comments, threaded',

    author=__author__,
    author_email=__email__,
    url=__url__,

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

    license=__license__,
    include_package_data=True,
    zip_safe=False
)

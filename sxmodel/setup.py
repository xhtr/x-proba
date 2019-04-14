from setuptools import setup


setup(
    name='sxmodel',
    version='1.0.0',
    description='The data model',
    packages=['sxmodel'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'psycopg2cffi',
    ],
    tests_require=[
        'pytest-flask',
        'pytest-cov',
    ],
)

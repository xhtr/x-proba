from setuptools import setup


setup(
    name='sxadapter',
    version='1.0.0',
    description='The adapter',
    packages=['sxadapter'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        '',
    ],
    tests_require=[
        'pytest-flask',
        'pytest-cov',
    ],
)

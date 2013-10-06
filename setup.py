setup(
    name='UniversalClient',
    version='0.5.0',
    author='David Greisen',
    author_email='dgreisen@gmail.com',
    packages=['universalclient'],
    url='http://pypi.python.org/pypi/UniversalClient/',
    license='LICENSE.txt',
    description='A Universal REST api client for python.',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests>=2.0.0",
        "rauth>=0.6.2",
    ],
)
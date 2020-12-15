from setuptools import setup

setup(
    name='myfunc',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:/sandeepmj/pipping.git',
    author='Sandeep Junnarkar',
    author_email='sandeep@journalism.cuny.edu',
    license='unlicense',
    packages=['hello"],
    zip_safe=False
)

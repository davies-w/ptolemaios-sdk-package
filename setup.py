from setuptools import setup

setup(
        name='ptolemaios',
        version='0.0.1',
        description='My private package from private github repo',
        url='git@github.com:davies-w/ptolemaios-sdk-package.git',
        author='Winton Davies',
        author_email='wdavies@cs.stanford.edu',
        license='unlicense',
        requirements=['numpy']
        packages=['ptolemaios'],
        zip_safe=False
    )

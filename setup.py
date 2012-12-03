from setuptools import setup, find_packages

try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    LONG_DESCRIPTION = None

setup(
    name='gears-at-notation',
    version='0.1',
    url='https://github.com/gears/gears-at-notation',
    license='ISC',
    author='Yasha Borevich',
    author_email='j.borevich@gmail.com',
    description='Alternative dependencies parser for gears',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        #'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3.2',
    ],
)

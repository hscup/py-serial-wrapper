from distutils.core import setup

setup(
    name='serialpy',
    version='0.1.0',
    scripts=['serialpy.py'],
    url='https://github.com/hscup/py-serial-wrapper',
    license='LICENSE',
    description='Pyserial wrapper which enable to initiate using serialnumber',
    long_description=open('README.md').read(),
    install_requires=[
        "pyserial==3.4"
    ],
)
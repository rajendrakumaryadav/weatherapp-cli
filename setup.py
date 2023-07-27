from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()
setup(
    name='cli-script',
    version='0.0.1',
    packages=[''],
    url='github.com',
    license='MIT',
    author='rajendrayadav',
    author_email='rajendra.ecti@gmail.com',
    description='Sample',
    install_requires=[
        required
    ],
    entry_points={
        'console_scripts': [
            'main=main:main'
        ],
    }
)

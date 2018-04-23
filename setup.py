import setuptools


setuptools.setup(
    install_requires=[
        'Flask',
    ],

    setup_requires=[
        'Flask==0.12.2',
        'pytest-runner',
    ],

    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-flakes',
        'pytest-pythonpath',
        'pytest-sugar',
    ],

    name='task2',
    version='0.0.1',

    author='Paulo R',
    author_email='proberto.macedo@gmail.com',

    description='Task2.',
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(exclude='tests'),

    entry_points={
        'console_scripts': [
            'task2-http-server = task2.server:main',
        ],
    },

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)

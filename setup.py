# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='hsimpy',
    version='1.0.0',
    description='Rather than just saying a password is "weak" or "strong", How Secure is My Password? lets your users know how long it would take someone to crack their password.',
    license='MIT',
    url='https://github.com/robsongajunior/hsimpy',
    author='Robson Gomes de Araújo Júnior',
    author_email='robson.junior@gmail.com',
    maintainer='Robson Júnior',
    author_email='robson.junior@gmail.com',
    keywords=[
        'validation',
        'pwd',
        'password',
        'strenght',
        'secure'
    ],
    install_requires=open('requirements.txt').read(),
    tests_require=open('requirements-test.txt').read(),
    dependency_links=[],
    packages=find_packages(),
    data_files = [],
)

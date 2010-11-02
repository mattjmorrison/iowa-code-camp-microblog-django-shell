from setuptools import setup

setup(
    name="icc_sample",
    version="0.1",
    description="Django app using buildout",
    author="Matthew J. Morrison",
    package_dir={'': 'src'},
    install_requires = (
        'django==1.2.3',
        'south',
        'mock'),
    entry_points=("""
        [console_scripts]
        manage=manage:main
    """)    
)
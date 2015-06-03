from setuptools import setup

setup(
    name='munge',
    version='0.1',
    py_modules=['munge'],
    include_package_data=True,
    install_requires=[
        'click>=4.0',
        'tablib>=0.10.0'
    ],
    entry_points="""
        [console_scripts]
        munge=munge.cli:convert
    """
)

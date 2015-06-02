from setuptools import setup

setup(
    name='converter',
    version='0.1',
    py_modules=['cli'],
    include_package_data=True,
    install_requires=[
        'click>=4.0',
        'tablib>=0.10.0'
    ],
    entry_points="""
        [console_scripts]
        converter=cli:convert
    """
)

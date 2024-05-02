from setuptools import setup, find_packages

setup(
    name='CTR BENCHMARK AUTOMATION',  # Your project's name
    version='0.1',  # Your project's version
    author='Meher Nigar',  # Your name
    author_email='mehernigarcu@gmail.com',  # Your email
    description='Automation tool for CTR benchmarking using Google Search Console data.',  # Short description
    packages=find_packages(),  # Automatically find all packages
    py_modules=['Main'],  # Your main module
    install_requires=[
        'pandas',  # Data manipulation
        'requests',  # HTTP for Humans
        'aiohttp',  # Asynchronous HTTP client/server
        'beautifulsoup4',  # HTML and XML parsing
        'google-searchconsole@git+https://github.com/joshcarty/google-searchconsole',  # Google Search Console API client
    ],
    entry_points={
        'console_scripts': [
            'ctr_benchmark=Main:main'  # Command line script entry point
        ]
    }
)

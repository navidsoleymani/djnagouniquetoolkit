import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='DjangoUniqueToolkit',
    version='0.1.0',
    author='Hydra',
    author_email='navidsoleymani@ymail.com',
    description=(
       ""
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/navidsoleymani/djangouniquetoolkit',
    project_urls={
        'Documentation': 'https://github.com/navidsoleymani/djangouniquetoolkit',
        'Bug Reports': 'https://github.com/navidsoleymani/djangouniquetoolkit/issues',
        'Source Code': 'https://github.com/navidsoleymani/djangouniquetoolkit',
    },
    license='MIT',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    include_package_data=True,
    classifiers=[
        'Framework :: Django :: 5.2',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Django>=4.2,<6.0',
        'djangorestframework>=3.14,<4.0',
        'pydantic>=2.0,<3.0',
        'markdown>=3.0,<4.0',
        'django-filter>=23.0,<25.0',
        'django-simple-history>=3.0,<4.0',
        'Pillow>=9.0,<11.0',
        'httpx>=0.24,<1.0',
    ],
    extras_require={
        'dev': [
            'tox',
            'pytest',
            'pytest-cov',
            'flake8',
            'mypy',
        ],
    },
)

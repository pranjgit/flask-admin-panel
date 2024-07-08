from setuptools import setup, find_packages

setup(
    name='flask_admin_panel',
    version = "0.0.1",
    packages=find_packages(),
    include_package_data=True,
    
    install_requires=[
        'Flask',
        'flask-restx',
        'Flask-SQLAlchemy',
        'Flask-JWT-Extended',
        'Flask-Injector',
        'flask-marshmallow',
        'Flask-Migrate',
        'Flask-WTF',
        'WTForms',
        'SQLAlchemy',
        'WTForms-Alchemy',
        'WTForms-Components'
        # Add other dependencies here
    ],
    package_data={
        'flask_admin_panel': ['flask_admin_panel/templates/flask_admin_panel/*.html']
    },
    author='Pranjal Gharat',
    author_email='pranjgit@gmail.com',
    description='Simple Admin Panel for Flask',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pranjgit/flask-admin-panel',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

from setuptools import setup, find_packages

setup(
    name='OdooXMLRPCLibrary',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'xmlrpc',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'odoo_library = odoo_library.create_order:main',
            'create_contact = odoo_library.create_contact:main',
        ],
    },
    author='Aditya Irri',
    author_email='adityairri@gmail.com',
    description='OdooXMLRPCLibrary is a Python library that simplifies interaction with the Odoo ERP system using XML-RPC API. With modules like create_order and create_contact, it provides an easy-to-use interface for managing rental orders and contacts in the Odoo platform. Whether youre integrating Odoo functionality into your application or automating business processes, OdooXMLRPCLibrary streamlines the communication process, making it efficient and developer-friendly.',
    url='https://github.com/yourusername/OdooXMLRPCLibrary',
    license='MIT',
)

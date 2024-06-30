from setuptools import setup, find_packages

setup(
    name='obiwandre',
    version='0.1.1.0.0',
    packages=find_packages(),
    install_requires=[
        # lista de dependências
        "python-dotenv==1.0.1"
    ],
    author='André Augusto Pereira',
    author_email='andre.diligente@gmail.com',
    description='Biblioteca de instalação de módulos privados',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/obiwandre/obiwandre',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
from setuptools import setup
setup(
    name='snp500',
    version='0.0',
    description='S&P 500 tickers',
    url='git@github.com:kthouz/SnP500Tickers.git',
    author='Camille Girabawe',
    author_email='cgirabawe@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas'
        ],
    zip_safe=True
)

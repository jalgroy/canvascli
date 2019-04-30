from setuptools import find_packages, setup
import pathlib

here = pathlib.Path(__file__).parent
readme = (here / 'README.md').read_text()

print(find_packages())

setup(
    name='canvas-cli',
    version='1.0.5',
    description='CLI for the Canvas LMS',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/jalgroy/canvascli',
    author='Joakim Algrøy and Petter Daae',
    license='MIT',
    packages=['canvascli'],
    include_package_data=True,
    install_requires=['docopt', 'html2text', 'canvasapi'],
    entry_points={
        'console_scripts': [
            'canvascli=canvascli.__main__:main',
        ]
    },
)
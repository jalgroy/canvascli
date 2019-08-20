from distutils.core import setup
setup(
  name = 'ccli',         # How you named your package folder (MyLib)
  packages = ['ccli'],   # Chose the same as "name"
  version = '0.0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'CLI for the Canvas LMS',   # Give a short description about your library
  author = 'Joakim Algrøy and Petter Daae',                   # Type in your name
  author_email = 'petter.daae@gmail.com',
  url = 'https://github.com/jalgroy/canvascli',   # Provide either the link to your github or to your website
  install_requires=[            # I get to this in a second
    'docopt',
    'canvasapi',
    'html2text'
  ],
  entry_points={
      'console_scripts': [
          'ccli = ccli.__main__:main'
      ]
  }
)
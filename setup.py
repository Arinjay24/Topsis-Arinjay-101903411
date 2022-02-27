from distutils.core import setup
setup(
  name = 'Topsis-Arinjay-101903411',         # How you named your package folder (MyLib)
  packages = ['Topsis-Arinjay-101903411'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'It is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion. An assumption of TOPSIS is that the criteria are monotonically increasing or decreasing. Normalisation is usually required as the parameters or criteria are often of incongruous dimensions in multi-criteria problems. Compensatory methods such as TOPSIS allow trade-offs between criteria, where a poor result in one criterion can be negated by a good result in another criterion. This provides a more realistic form of modelling than non-compensatory methods, which include or exclude alternative solutions based on hard cut-offs. An example of application on nuclear power plants is provided in',   # Give a short description about your library
  author = 'Arinjay Shukla',                   # Type in your name
  author_email = 'ashukla1_be19@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/Arinjay24/Topsis-Arinjay-101903411',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Arinjay24/Topsis-Arinjay-101903411/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['Easy to Use', 'Fascinating concept'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'math',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

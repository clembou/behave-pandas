import setuptools

setuptools.setup(
    name="behave-pandas",
    version="0.1.0.dev1",
    url="https://github.com/clembou/behave-pandas",

    author="Clément Bouscasse",
    author_email="clement.bouscasse@gmail.com",

    description="Provides helper function to help converting behave tables into pandas dataframes and vice versa.",
    long_description="Pandas makes working with tabular data easy, and Gherkin makes testing tabular data easy. "
        "By making it possible to convert gherkin tables into data frames, "
        "behave becomes a very useful testing tool for data workloads.",

    packages=setuptools.find_packages(),

    install_requires=['behave', 'pandas', 'tabulate'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
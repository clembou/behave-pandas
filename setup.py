import setuptools

try:
    from pypandoc import convert

    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setuptools.setup(
    name="behave-pandas",
    version="0.1.0.dev2",
    url="https://github.com/clembou/behave-pandas",

    author="Clément Bouscasse",
    author_email="clement.bouscasse@gmail.com",

    description="Provides helper functions to help converting behave tables into pandas dataframes and vice versa.",
    long_description=read_md('README.md'),

    packages=setuptools.find_packages(),

    install_requires=['behave', 'pandas', 'tabulate'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    license='MIT',
    keywords='behave pandas testing bdd',
    python_requires='>=3.5',
)

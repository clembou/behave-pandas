import setuptools

setuptools.setup(
    name="behave-pandas",
    version="0.3.0",
    url="https://github.com/clembou/behave-pandas",
    author="Clément Bouscasse",
    author_email="clement.bouscasse@gmail.com",
    description="Provides helper functions to help converting behave tables into pandas dataframes and vice versa.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["behave", "pandas", "tabulate"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT",
    keywords="behave pandas testing bdd",
    python_requires=">=3.5",
)

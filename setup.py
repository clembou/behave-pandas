import setuptools

setuptools.setup(
    name="behave-pandas",
    version="1.0.0-dev",
    url="https://github.com/clembou/behave-pandas",
    author="Clément Bouscasse",
    author_email="clement.bouscasse@gmail.com",
    description="Provides helper functions to help converting behave tables into pandas dataframes and vice versa.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["behave", "pandas>=0.21", "tabulate"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    license="MIT",
    keywords="behave pandas testing bdd",
    python_requires=">=3.8",
)

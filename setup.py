"""Provider for Faker which adds fake nonprofit information."""

import setuptools

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()  # pylint: disable=invalid-name
except FileNotFoundError:
    # pylint: disable=invalid-name
    long_description = (
        "Provider for [Faker](https://faker.readthedocs.io/) which adds fake "
        "nonprofit information."
    )

setuptools.setup(
    name="faker-nonprofit",
    version="1.0.0",
    author="Aaron Crosman, Allison Letts, Paul Prescod",
    author_email="DatagenToolkitTeam@example.invalid",
    description="Provider for Faker which adds fake nonprofit information.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SFDO-Community-Sprints/Snowfakery-Nonprofit",
    packages=setuptools.find_packages(),
    install_requires=["faker"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)

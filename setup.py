import setuptools

from setup_utils import get_requirements, get_dev_requirements

requirements = get_requirements()
dev_requirements = get_dev_requirements()

setuptools.setup(
    name="wrapper_process",
    version="0.1",
    description="Wrapper module for python sub_process",
    python_requires=">=3.7",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    install_requires=[requirements],
    extras_require={"dev": [dev_requirements]},
)

""" Setup script
"""
from pathlib import Path

from setuptools import setup, find_packages

PACKAGE_NAME = "pydantic-mongo"
MAJOR_VERSION = 0
MINOR_VERSION = 1
PATCH_VERSION = 0

HERE = Path(__file__).parent.resolve()


def update_package_version(path: Path, version: str):
    """Overwrite/create __init__.py file and fill __version__"""
    with open(path / "VERSION", "w") as version_file:
        version_file.write(f"{version}\n")


def build_version():
    """Build dynamic version and update version in package"""
    version = f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"

    update_package_version(HERE / "pkg" / "pydantic_mongo", version=version)

    return version


def get_long_description(base_path: Path):
    """Get long package description"""
    return (base_path / "README.md").read_text(encoding="utf-8")


setup(
    name=PACKAGE_NAME,
    version=build_version(),
    description="Pydantic basic model for MongDB entries",
    long_description=get_long_description(HERE),
    long_description_content_type="text/markdown",
    url="https://github.com/2read-online/pydantic-mongodb",
    author="Alexey Timin",
    author_email="atimin@gmai.com",
    package_dir={"": "pkg"},
    package_data={"": ["VERSION"]},
    packages=find_packages(where="pkg"),
    python_requires=">=3.8",
    install_requires=["pydantic==1.8.2", "pymongo==3.12.0"],
    extras_require={
        "test": [
            "pytest==6.2.4",
        ],
        "lint": [
            "pylint==2.9.6",
        ],
    },
)

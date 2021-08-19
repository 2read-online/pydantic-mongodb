""" Pydantic Mongo
"""
from .mongo_model import OID, MongoModel

__all__ = ["OID", "MongoModel"]


def _load_version() -> str:
    """Load version from VERSION file"""
    from pathlib import Path  # pylint: disable=import-outside-toplevel

    here = Path(__file__).parent.resolve()
    with open(str(here / "VERSION")) as version_file:
        return version_file.read().strip()


__version__ = _load_version()

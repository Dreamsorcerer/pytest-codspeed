__version__ = "3.0.0b0"
# We also have the semver version since __version__ is not semver compliant
__semver_version__ = "3.0.0-b0"

from .plugin import BenchmarkFixture

__all__ = ["BenchmarkFixture", "__version__"]

# company/__init__.py

# Import the main Company class for easy access
from .base_simulator import BaseSimulator

# Import specific submodule classes
from .gbm.gbm_simulator import GBMSimulator

# Import version information for the package
from .version import __version__  # Ensure version.py contains this variable

# Print the package version for confirmation (optional)
print(f"Company package version: {__version__}")
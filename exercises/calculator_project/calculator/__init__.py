# Pre-importing functions to expose them at the package level
from .arithmetic import addition, subtraction, multiplication, division
from .advanced import power, square_root, factorial
from .constants import pi, e

# Defining what gets exported during a wildcard (*) import
__all__ = ['addition', 'subtraction', 'multiplication', 'division', 'power', 'square_root', 'factorial', 'pi', 'e']
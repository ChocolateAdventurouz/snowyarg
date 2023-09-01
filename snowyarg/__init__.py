"""
snowyarg - Simple and basic argument parser library in Python
Author: Karapatakis Aggelos 
<aggeloskarapatakis@outlook.com.gr>

snowyarg is only based on the intergreated sys module
"""

from .argument import Argument
from .helpargument import HelpArgument
__all__ = ("Argument", "HelpArgument")
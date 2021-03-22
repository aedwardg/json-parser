import os
import sys
from pathlib import Path


def setup():
    # Allow examples to be run without directly installing as a package
    parent_dir = Path(__file__).absolute().parent.parent
    sys.path.append(os.path.join(os.path.dirname(__file__), parent_dir))
    from jparse.parser import JSONParser

    return JSONParser

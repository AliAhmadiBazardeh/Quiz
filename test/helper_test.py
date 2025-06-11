import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utilities.helper import simple_slugify

def test_simple_slugify():
    assert simple_slugify("Red Toyota Corolla 2022") == "red-toyota-corolla-2022"
    assert simple_slugify("  Hello@@ World!!  ") == "hello-world"
    assert simple_slugify("سلام دنیا") == "سلام-دنیا"

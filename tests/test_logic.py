import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from broken_code.logic import is_even

def test_even_true():
    assert is_even(4) is True

def test_even_false():
    assert is_even(3) is True  # 의도된 실패

from piskvorky import vyhodnot_stav
from piskvorky import tah_hrace
from ai import tah_pocitace
from piskvorky import pole

import pytest

def test_vyhodnot_stav():
    assert vyhodnot_stav('----------------------') == '-'

def test_vyhodnot_stav2():
    assert vyhodnot_stav('----------------------') != 'o'

def test_vyhodnot_stav3():
    assert vyhodnot_stav('---------------') == '-'

def test_tah_hrace():
    assert tah_hrace('--', 1) == '-x'

def test_tah_hrace2():
    with pytest.raises(Exception):
        assert tah_hrace('--', 8)

def test_tah_pocitace():
    with pytest.raises(TypeError):
         tah_pocitace(20, znak='o')

def test_tah_pocitace2():
    with pytest.raises(TypeError):
         tah_pocitace('--------------------', znak=1)

def test_tah_pocitace_delka():
         tah_pocitace('------', znak='o')

def test_tah_pocitace_pole0():
    with pytest.raises(LookupError):
         tah_pocitace('', znak='o')

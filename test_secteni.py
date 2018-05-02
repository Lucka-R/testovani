from secteni import secti

def test_secti():
    assert secti(1, 2) == 3

def test_sectidvoucif():
    assert secti(89, 42) == 131

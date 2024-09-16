
def pytest_generate_tests(metafunc):
    if "num_dice" in metafunc.fixturenames:
        metafunc.parametrize("num_dice", range(6))
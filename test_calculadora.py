from calculadora import suma, resta, dividir
import pytest
from hypothesis import given
import hypothesis.strategies as st

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2

@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 5),
    (10, -5, 5),
    (0, 0, 0),
    (2, 6, 10),
])
def test_suma_parametrizada(a, b, resultado):
    assert suma(a, b) == resultado


@pytest.mark.hypothesis
@given(st.integers(), st.integers())
def test_suma_conmutativa(a, b):
    assert suma(a, b) == suma(b, a)

@given(st.integers())
def test_resta_identidad(a):
    assert resta(a, a) == 0

@given(st.integers(), st.integers())
def test_division(a, b):
    assert dividir(a, b) * b == a

# --hypothesis-show-statistics
# pytest -v -k "suma"
# pytest test_calculadora.py::test_suma -v
# pytest --lf --ff para test que
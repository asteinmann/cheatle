from cheatle import __version__
from cheatle import WordleSolver
import pytest

@pytest.fixture
def solver():
    yield WordleSolver()

def test_version():
    assert __version__ == '0.1.0'

def test_solver(solver):
    answers = solver.get_list('.....','')
    assert len(answers) == 10232
    answers = solver.get_list('chan.','t')
    assert len(answers) == 1
    answers = solver.get_list('chan.','')
    assert len(answers) == 3

    


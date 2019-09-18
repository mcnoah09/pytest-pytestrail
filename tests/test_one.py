from pytest_pytestrail import pytestrail
import pytest


@pytestrail.case('C79')
def test_one():
    assert True


@pytestrail.case('C10001')
def test_two():
    assert True


case_one = pytestrail.steps_case('C80')


@case_one.step(1)
def test_step_one():
    assert True


@case_one.step(2)
def test_step_two():
    assert False


case_two = pytestrail.steps_case('C10002')


@case_two.step(1)
def test_step_three():
    assert True


@case_two.step(2)
def test_step_four():
    assert True


@pytest.mark.parametrize('data', [pytestrail.param(1, 'C81'), pytestrail.param(2, 'C82')])
def test_three(data):
    assert data


@pytest.mark.parametrize('data', [pytestrail.param(1, 'C83', 1), pytestrail.param(2, 'C83', 2)])
def test_four(data):
    assert data


@pytest.mark.parametrize('data', pytestrail.params('C84', [1, 2, 3, 4, 5]))
def test_five(data):
    assert data

from examples.identifier import Identifier
import pytest

@pytest.mark.parametrize(

    'identif', 
    [
        pytest.param('a'),
        pytest.param('ab'),
        pytest.param('abcd'),
        pytest.param('abcde'),
        pytest.param('abcdef'),
        pytest.param('abcdeg'),
        pytest.param('a1'),

    ]
)

def test_all_valid_cases(identif):
    is_valid = Identifier().validate_identifier(identif)

    assert is_valid is True

def test_exception_raised():

    with pytest.raises(ValueError) as error:
        Identifier().validate_identifier('')

    assert str(error.value) == 'Identificador inválido'
 

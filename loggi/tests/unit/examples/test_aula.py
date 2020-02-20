from examples.identifier import Identifier

def test_case_test_01():
    identify = Identifier()
    is_valid = identify.validate_identifier('ab')

    assert is_valid is True

def test_case_02():
    is_valid = Identifier().validate_identifier('')
    
    assert is_valid is False

def test_case_07():
    is_valid = Identifier().validate_identifier('abcde')

    assert is_valid is True

def test_case_08():
    is_valid = Identifier().validate_identifier('abcdef')

    assert is_valid is True

def test_case_03():
    is_valid = Identifier().validate_identifier('abcdefg')

    assert is_valid is False

def test_case_04():
    is_valid = Identifier().validate_identifier('1a')

    assert is_valid is False

def test_case_05():
    is_valid = Identifier().validate_identifier('a1')

    assert is_valid is True

def test_case_06():
    is_valid = Identifier().validate_identifier('açaí')

    assert is_valid is False


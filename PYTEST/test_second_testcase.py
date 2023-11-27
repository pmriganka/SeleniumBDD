import pytest

def get_data():
    return [
        ("sgdfhasdghfg@gmail.com", "sadfsdaf"),
        ("sgdfherfl.com", "saeqwdaf")
    ]

@pytest.mark.parametrize("username, password", get_data())
def test_dologin(username , password):
    print(username, "---" , password)
    

def test_validate_titles():
    #pip install pytest-soft-assertions
    #python -m pytest test_second_testcase.py -s -v --soft-asserts
    expected_title = "abc"
    actual_title = "def"
    assert expected_title == actual_title, "ugasfugsadgfusgduf"
    assert False, "dsfsadfaff"
    
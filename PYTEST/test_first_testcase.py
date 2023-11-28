import pytest

# pytest functions will start with test
# Execute using "python -m pytest" 
# For details use -s -v
#-k for selecting particular tests, deselect -k "not login"

'''
def setup_module(module):
    print("Creating DB Connection")

def setup_function(function):
    #setup will be used before running any test
    print("Launching browser")
    
def teardown_function(function):
    #teardown will be used before quitting any test
    print("Quitting test")

def test_dologin():
    print("Executing login test")
    

def test_userlogin():
    print("Executing user login  test")

'''

@pytest.fixture(scope='module')
def setup():
    print("Creating DB connection")
    yield
    print("Closing DB connection")
    
@pytest.fixture(scope='function')
def wrapper():
    print("Launching browser")
    yield
    print("Quitting browser")

@pytest.mark.usefixtures("setup", "wrapper")
def test_dologin():
    print("Executing login test")
    

def test_userlogin(setup, wrapper):
    print("Executing user login  test")
    
def test_nextlogin(setup, wrapper):
    print("Executing next  test")
   
   
@pytest.mark.skip()    
def test_skip():
    print("Skip test")



    
from flask_app import *

def test_country():
    assert country() == 'India'

def test_city():
    assert city() == 'Bangalore'

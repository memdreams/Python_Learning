from nose.tools import *
from bin.app import app
import sys
if sys.version_info[0] < 3:
    from tools import assert_response
else:
    from test.tools import assert_response


def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status='404')

    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # make sure default values work for the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")

    # test that we get expected values
    data = {'name': 'Zed', 'greed': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")

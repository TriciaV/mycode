"""
The pytest library is rather extensive. 
Many other tests are possible, so be sure to review https://docs.pytest.org/en/stable/ if you haven't already.
"""
# import our code called isspace.py
import issspace
# import our pytest suite
import pytest

# our tests are now in a dedicated file
def test_astros():
    # request cannot perform sending an HTTP get
    # we cannot run this sort of test --> assert issspace.astros() == "Network access not allowed during testing!"
    # if we do, it will cause a runtime error to be thrown and pytest will crash
    # therefore we must tell pytest to expect a runtime error
    with pytest.raises(RuntimeError) as slappysquirrel:
        # telling pytest to run the astros() function within the file issspace.py
        # because it's nested in the with statement, pytest understands this will return a runtime error
        # However, rather than crashing pytest, pytest will keep running because it knows this is expected behavior
        issspace.astros()

    assert "Network access not allowed" in str(slappysquirrel.value)
    # here we are asserting that the slappysquirrel object created by pytest contains the string "Network access not allowed"



from my_lambdata.assignment1 import WrangledFrame


def test_add_state_names():

    wf = WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    assert list(wf.columns) == ['abbrev']

    wf.add_state_names()
    # ensure there is a "name" column
    assert list(wf.columns) == ['abbrev', 'name']

    # ensure the values of WF are specifc classes / values (string, "California")
    assert wf["name"][0] == "Cali"
    assert wf["abbrev"][0] == "CA"
        
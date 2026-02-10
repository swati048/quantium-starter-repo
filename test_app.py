from app import app


# ---------- Test 1: Header exists ----------
def test_header_present(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Pink Morsel Sales"


# ---------- Test 2: Visualization exists ----------
def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


# ---------- Test 3: Region picker exists ----------
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    picker = dash_duo.find_element("#region-filter")
    assert picker is not None

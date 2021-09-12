from gale_shapley import stable_match

def test_stable_match():
    d1, d2, d3, d4 = "d1", "d2", "d3", "d4"
    e1, e2, e3, e4 = "e1", "e2", "e3", "e4"

    d_pref = {
        d1: [e4, e3, e1, e2],
        d2: [e2, e1, e4, e3],
        d3: [e1, e2, e3, e4],
        d4: [e1, e2, e3, e4],
    }
    e_pref = {
        e1: [d2, d3, d1, d4],
        e2: [d3, d2, d1, d4],
        e3: [d3, d1, d2, d4],
        e4: [d1, d2, d3, d4],
    }

    want = {(d1, e4), (d2, e1), (d3, e2), (d4, e3)}
    got = stable_match(e_pref, d_pref)
    assert got == want

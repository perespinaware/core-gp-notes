"""Helpers for writing AKT cases compactly. See build_cases.py."""
def G(ask, find, key, clue, extra=None):
    return [ask, find, key, clue] + ([extra] if extra else [])

def step(s, o, a, e, why, solo, bad=None, good=None):
    assert len(o) == 5 and len(why) == 5 and 0 <= a < 5, s
    assert why[a] == "" and all(why[i] for i in range(5) if i != a), ("why", s)
    d = {"s": s, "o": o, "a": a, "e": e, "why": why, "solo": solo}
    if bad:
        assert a not in bad, ("bad on the answer", s); d["bad"] = {str(k): v for k, v in bad.items()}
    if good: d["good"] = good
    return d

def case(cid, topic, cat, title, who, open_, items, steps, lesson, take, limit=4, mins=4, prompt=None):
    assert 5 <= len(items) <= 8 and any(i[2] for i in items) and len(steps) >= 3, cid
    return cid, {"topic": topic, "cat": cat, "title": title, "mins": mins, "who": who, "open": open_,
        "gather": {"prompt": prompt or f"You have time for {limit} of these. Choose the ones most likely to change your management.", "limit": limit, "items": items},
        "steps": steps, "lesson": lesson, "take": take}

"""Student examples for the W5 optional challenge tasks."""

import numpy as np


def test_my_summarize_case(summarize_values):
    values = [4, 0, 4, -2]
    before = values.copy()

    result = summarize_values(values)

    assert result == {
        "unique": [4, 0, -2],
        "counts": {4: 2, 0: 1, -2: 1},
        "repeated": {4},
    }
    assert values == before


def test_my_apply_changes_case(apply_changes):
    original = {"x": 1, "y": 2}
    updates = [("x", 9), ("x", 1), ("new", 4)]
    removals = ["new", "y"]
    before_original = original.copy()
    before_updates = updates.copy()
    before_removals = removals.copy()

    result = apply_changes(original, updates, removals)

    assert result == {"record": {"x": 1}, "changed": {"y"}}
    assert original == before_original
    assert updates == before_updates
    assert removals == before_removals


def test_my_compare_measurements_case(compare_measurements):
    ids = ["up", "down", "edge"]
    baseline = np.array([1, 8, 4], dtype=np.int16)
    current = np.array([5, 2, 6], dtype=np.int16)
    before_baseline = baseline.copy()
    before_current = current.copy()

    result = compare_measurements(ids, baseline, current, 4)

    np.testing.assert_array_equal(result["delta"], np.array([4, -6, 2]))
    assert result["alerts"] == ["down"]
    assert result["normal"] == {"up": 5, "edge": 6}
    assert ids == ["up", "down", "edge"]
    np.testing.assert_array_equal(baseline, before_baseline)
    np.testing.assert_array_equal(current, before_current)

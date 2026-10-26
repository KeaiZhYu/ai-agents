"""Student examples for the W5 optional challenge tasks."""


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

"""W4 学生测试：独立的追加方案。

自选输入（与课堂例子不同）：
    source = {"seed": 123, "sample_sizes": [250, 500, 1000, 2000]}
    make_variant(source, seed=7, index=1, replacement=750)
预期（按修改规则独立写出，不调用被测实现生成）：
    {"seed": 7, "sample_sizes": [250, 750, 1000, 2000]}

每个测试通过函数参数接收课程 fixture make_variant，不直接 import 实现，
这样 --impl 才能切换被检查的候选。
"""


def _source():
    return {"seed": 123, "sample_sizes": [250, 500, 1000, 2000]}


def _expected():
    return {"seed": 7, "sample_sizes": [250, 750, 1000, 2000]}


def test_updates_only_requested_values(make_variant):
    source = _source()

    result = make_variant(source, seed=7, index=1, replacement=750)

    assert result == _expected()


def test_source_content_stays_as_before(make_variant):
    source = _source()

    make_variant(source, seed=7, index=1, replacement=750)

    assert source == {"seed": 123, "sample_sizes": [250, 500, 1000, 2000]}


def test_result_owns_new_dictionary_and_list(make_variant):
    source = _source()

    result = make_variant(source, seed=7, index=1, replacement=750)

    assert result is not source
    assert result["sample_sizes"] is not source["sample_sizes"]


def test_later_changes_to_result_do_not_reach_source(make_variant):
    source = _source()
    result = make_variant(source, seed=7, index=1, replacement=750)

    result["seed"] = 8
    result["sample_sizes"][1] = 775
    result["sample_sizes"].append(4000)

    assert result == {"seed": 8, "sample_sizes": [250, 775, 1000, 2000, 4000]}
    assert source == {"seed": 123, "sample_sizes": [250, 500, 1000, 2000]}


def test_two_identical_calls_can_be_changed_separately(make_variant):
    source = _source()

    first = make_variant(source, seed=7, index=1, replacement=750)
    second = make_variant(source, seed=7, index=1, replacement=750)

    assert first == _expected()
    assert second == _expected()
    assert first == second
    assert first is not second
    assert first["sample_sizes"] is not second["sample_sizes"]

    first["seed"] = 8
    first["sample_sizes"][1] = 775

    assert second == _expected()
    assert source == {"seed": 123, "sample_sizes": [250, 500, 1000, 2000]}


def test_unchanged_parameters_still_return_independent_plan(make_variant):
    source = _source()

    first = make_variant(source, seed=123, index=1, replacement=500)
    second = make_variant(source, seed=123, index=1, replacement=500)

    assert first == source
    assert second == source
    assert first is not source
    assert second is not source
    assert first is not second
    assert first["sample_sizes"] is not source["sample_sizes"]
    assert second["sample_sizes"] is not source["sample_sizes"]
    assert first["sample_sizes"] is not second["sample_sizes"]

    first["sample_sizes"][1] = 5000

    assert second == {"seed": 123, "sample_sizes": [250, 500, 1000, 2000]}
    assert source == {"seed": 123, "sample_sizes": [250, 500, 1000, 2000]}


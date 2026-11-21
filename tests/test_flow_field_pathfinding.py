import pytest
import math
from gameplay import flow_field_pathfinding as mod

CASES = [
    ("exits", 'm.merge_exits([3, 1, 2]) == 1'),
    ("diag", 'm.diagonal_cost(1) == approx(1.414, abs=1e-3)'),
    ("inc", 'm.incremental(1, 2, True) == 2'),
    ("portal", 'm.portal_link(3, 1) == 1'),
    ("slope", 'm.slope_cost(1, 2) == approx(0.5)'),
    ("sep", 'm.separation(2, 3) == 6'),
    ("inflate", 'm.inflate(1, 0.5) == 2'),
    ("obstacle", 'm.update_on_obstacle(True) is True'),
    ("local", 'm.local_recalc(True) is True'),
    ("layer", 'm.interp_layers(0, 10, 0.5) == approx(5.0)'),
    ("step", 'm.step_cost(1, 1) == approx(2.0)'),
    ("key", 'm.flow_key(3, 2) == "3:2"'),
    ("queue", 'm.queue_priority(5) == -5'),
    ("reach", 'm.reachable(5) is True'),
    ("dir", 'm.direction(1, 0) == (1, 0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})

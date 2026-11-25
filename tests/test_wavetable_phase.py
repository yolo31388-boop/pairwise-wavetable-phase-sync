import pytest
import av.wavetable_phase as mod

CASES = [
    ("index_by_rate", (1,)),
    ("per_note_state", (1,)),
    ("envelope_per_sample", (1,)),
    ("atomic_table_swap", (1,)),
    ("mip_by_f0", (1,)),
    ("release_tail_fill", (1,)),
    ("load_table", (1,)),
    ("note_on", (1,)),
    ("render_audio", (1,)),
    ("present_audio", (1,)),
    ("validate_render", (1,)),
    ("metrics_audio", (1,)),
    ("audit_audio", (1,)),
    ("fallback_audio", (1,)),
    ("determinism_audio", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

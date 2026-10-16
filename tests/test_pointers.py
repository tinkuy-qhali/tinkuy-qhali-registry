"""Every pointer must validate against schema/pointer.schema.json. Run: python -m pytest tests/ (inside the container)."""
import json, pathlib
import pytest
jsonschema = pytest.importorskip("jsonschema")
ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schema" / "pointer.schema.json").read_text(encoding="utf-8"))
POINTERS = sorted((ROOT / "pointers").glob("*.json"))

@pytest.mark.parametrize("path", POINTERS, ids=[p.stem for p in POINTERS])
def test_pointer_validates(path):
    jsonschema.validate(json.loads(path.read_text(encoding="utf-8")), SCHEMA)

def test_pointer_id_matches_filename():
    for p in POINTERS:
        assert json.loads(p.read_text(encoding="utf-8"))["pointer_id"] == p.stem

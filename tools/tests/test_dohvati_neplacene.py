import pytest
from unittest.mock import patch
from tools.dohvati_neplacene import tools_dohvati_neplacene

@patch("tools.dohvati_neplacene.get_neplaceni")
def test_tools_dohvati_neplacene(mock_get_neplaceni):

    mock_get_neplaceni.return_value = [
        {"id_racuni": 1, "id_korisnik": 1, "tip_racuna": "struja", "iznos": 100, "rok_uplate": "2024-07-01", "mjesec": "juli", "godina": 2024, "placeno": 0},
        {"id_racuni": 2, "id_korisnik": 1, "tip_racuna": "voda", "iznos": 50, "rok_uplate": "2024-07-05", "mjesec": "juli", "godina": 2024, "placeno": 0}
    ]

    result = tools_dohvati_neplacene(1)


    assert result["success"] is True
    assert isinstance(result["data"], list)
    assert len(result["data"]) == 2

    assert result["data"][0]["tip_racuna"] == "struja"
    assert result["data"][1]["tip_racuna"] == "voda"
import pytest
from unittest.mock import patch
from tools.dodaj_racun import tools_dodaj_racun
from database.exceptions import ValidationError, DatabaseError


@patch("tools.dodaj_racun.kreiraj_racun")
@patch("tools.dodaj_racun.normalizuj_input_mjeseca")
def test_tools_dodaj_racun_success(mock_normalizuj, mock_kreiraj):

    mock_normalizuj.return_value = "januar"

    result = tools_dodaj_racun(
        id_korisnik=1,
        tip_racuna="struja",
        iznos=150,
        rok_uplate="2026-03-01",
        mjesec="Januar",
        godina=2026
    )

    mock_normalizuj.assert_called_once_with("Januar")

    mock_kreiraj.assert_called_once_with(
        1,
        "struja",
        150,
        "2026-03-01",
        "januar",
        2026
    )

    assert result["success"] is True
    assert result["data"]["status"] == "success"
    assert result["data"]["message"] == "Racun kreiran"


@patch("tools.dodaj_racun.kreiraj_racun")
def test_tools_dodaj_racun_validation_error(mock_kreiraj):

    mock_kreiraj.side_effect = ValidationError("Tip racuna nije dozvoljen")

    result = tools_dodaj_racun(
        1,
        "pogresan_tip",
        100,
        "2026-03-01",
        "januar",
        2026
    )

    assert result["success"] is False
    assert result["error"] == "Tip racuna nije dozvoljen"
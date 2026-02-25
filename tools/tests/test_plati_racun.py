import pytest
from unittest.mock import patch
from tools.plati_racun import tools_plati_racun
from database.exceptions import ValidationError, NotFoundError

@patch("tools.plati_racun.plati_racun")
@patch("tools.plati_racun.normalizuj_input_mjeseca")
def test_tools_plati_racun_success(mock_normalizuj, mock_plati):
    mock_normalizuj.return_value = "februar"

    result = tools_plati_racun(
        tip_racuna="voda",
        mjesec="Februar",
        godina=2026
    )

    mock_normalizuj.assert_called_once_with("Februar")

    mock_plati.assert_called_once_with(1,
        "voda",
        "februar",
        2026
    )

    assert result["success"] is True
    
    assert result["data"]["status"] == "success"
    assert result["data"]["message"] == "Racun placen"  


@patch("tools.plati_racun.plati_racun")
@patch("tools.plati_racun.normalizuj_input_mjeseca")    
def test_tools_plati_racun_error(mock_normalizuj, mock_plati):
    
    mock_normalizuj.return_value = "juni"
    mock_normalizuj.side_effect = NotFoundError("Racun ne postoji ili je vec placen")

    result = tools_plati_racun("struja","januar",2026)
    assert result["success"] is False
    assert "Racun ne postoji" in result["error"]
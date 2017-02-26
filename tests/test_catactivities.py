# from mock import patch
from catinabox import catactivities
import pytest


def test__cat_nap__satisfying(mocker):
    nap_time = 300
    # with patch('time.sleep') as mock_sleep:
    #     catactivities.cat_nap(nap_time)
    #     mock_sleep.assert_called_once_with(nap_time)
    mock_sleep = mocker.patch('time.sleep')
    catactivities.cat_nap(nap_time)
    mock_sleep.assert_called_with(nap_time)


def test__cat_nap__not_satisfying(mocker):
    nap_time = 1
    mock_sleep = mocker.patch('time.sleep')

    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(nap_time)
    assert mock_sleep.call_count == 0

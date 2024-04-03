import pytest
from project import option, d_one_video, d_playlist

def test_option():
    assert option(10) == print("Invalid input")
    assert option(0) == print("Invalid input")

def test_d_one_video():
    with pytest.raises(Exception) as excinfo:
        d_one_video("https://youtube.com/playlist?list=PL7PEEXKl_KzYFpHIHitd6suxznbEicgfw&si=y7QaezW8gVfNSK6y")
        assert excinfo.value.message == 'Technical Error...'
        print(excinfo.value.message)

def test_d_playlist():
     with pytest.raises(Exception) as excinfo:
        d_playlist("https://youtube.com/playlist?list=PL7PEEXKl_KzYFpHIHitd6suxznbgfw&si=y7QaezW8gVfNSK6y")
        assert excinfo.value.message == 'Playlist does not exist'
        print(excinfo.value.message)


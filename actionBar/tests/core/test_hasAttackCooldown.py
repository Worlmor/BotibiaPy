import pathlib
from actionBar.core import hasAttackCooldown
from utils.image import load, RGBtoGray


currentPath = pathlib.Path(__file__).parent.resolve()
screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))


def test_should_return_True_when_hasCooldownByImg_return_True(mocker):
    mocker.patch('actionBar.core.hasCooldownByImg', return_value=True)
    result = hasAttackCooldown(screenshotImg)
    assert result == True


def test_should_return_False_when_hasCooldownByImg_return_False(mocker):
    mocker.patch('actionBar.core.hasCooldownByImg', return_value=False)
    result = hasAttackCooldown(screenshotImg)
    assert result == False
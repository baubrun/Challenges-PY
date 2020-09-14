import pytest
from shiritori import Shiritori


def test_shiritori():
    my_shiritori = Shiritori()
    my_shiritori.play("apple")
    assert my_shiritori.words == ["apple"]


def test_shiritori2():
    my_shiritori = Shiritori()
    my_shiritori.play("apple")
    my_shiritori.play("ear")
    assert my_shiritori.words == ["apple", "ear"]


def test_shiritori3():
    my_shiritori = Shiritori()
    my_shiritori.play("apple")
    my_shiritori.play("ear")
    my_shiritori.play("rhino")
    assert my_shiritori.words == ["apple", "ear", "rhino"]


def test_shiritori4():
    my_shiritori = Shiritori()
    my_shiritori.play("apple")
    my_shiritori.play("ear")
    my_shiritori.play("rhino")
    assert my_shiritori.play("corn") == "game over"

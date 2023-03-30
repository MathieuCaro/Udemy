import pytest
from tkinter import Tk, Label
from calculator import show


# Création d'une fenêtre de test Tkinter
@pytest.fixture
def window():
    root = Tk()
    label = Label(root, text="Test")
    label.pack()
    yield root
    root.destroy()


def test_show(window):
    # On simule l'appui sur le bouton "1"
    show("1")
    assert label_result.get() == "1"

    # On simule l'appui sur le bouton "2"
    show("2")
    assert label_result.get() == "12"

    # On simule l'appui sur le bouton "3"
    show("3")
    assert label_result.get() == "123"

    # On simule l'appui sur le bouton "+"
    show("+")
    assert label_result.get() == "123+"

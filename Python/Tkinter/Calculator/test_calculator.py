import pytest
import tkinter as tk  # tkinter: package for standard python interface
from calculator import string_to_calculate


def test_string_to_calculate():
    # Test addition
    assert string_to_calculate("2+2") == 4
    # Test multiplication
    assert string_to_calculate("6*7") == 42
    # Test division
    assert string_to_calculate("8/2") == 4
    # Test substraction
    assert string_to_calculate("50-23") == 27


"""
@pytest.fixture
def init_window():
    root = tk.Tk()
    root.geometry("200x100")
    return root


def test_init_window(qtbot):
    window = init_window()

    qtbot.addWidget(window)

    assert window.winfo_exists()
    assert window.winfo_geometry() == "200x100+0+0"
"""


def create_window():
    root = tk.Tk()
    root.geometry("200x100+0+0")
    return root


"""
def test_create_window():
    window_ = create_window()
    window_.winfo_exists()
    print(window_.geometry())
    assert window_.winfo_exists() == 1
    assert window_.geometry() == "200x100+0+0"
    window_.destroy()
"""


def test_window_geometry():
    root = tk.Tk()
    root.geometry("300x200+100+100")

    # Récupérer la géométrie de la fenêtre
    geometry = root.geometry()

    # TODO
    # doesn't work
    # assert geometry == "300x200+100+100"

    root.destroy()

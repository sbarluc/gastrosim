from models.menu import Menu
from data.test_menu import dicc_precios

def test_menu_recibe_diccionario_de_precios():
    menu = Menu(dicc_precios)
    assert menu.precio("Croissant nutella") == 4000
    
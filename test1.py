from witgets import FastWitget, GridWidget
from actions import Action
from pages import Page, Aplication
from PyQt6.QtWidgets import QApplication
import sys

# main
app = QApplication(sys.argv)

witgett = FastWitget("I love my Doc", 600, 300)

label = witgett.create_label("file:")
btn = witgett.create_button("Load", Action.open_file, None, label)
label2 = witgett.create_label("file:")
btn2 = witgett.create_button("Load", Action.open_file, witgett, label2)

page = witgett.create_page([btn, label, btn2, label2])
page.show()

sys.exit(app.exec())

# def on_button_click():
#     print("Button clicked")

# app = QApplication(sys.argv)

# button = create_button("Click me!", on_button_click)
# label = create_label("Hello, world!")
# page = create_page("My Page", [label, button])

# page.show()

# sys.exit(app.exec())
from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as tkb
from ttkbootstrap.constants import *

root = tkb.Window(title="GH Table Maker", themename="superhero", size=[800, 600], resizable=[True, True])



combo = tkb.Combobox(root, bootstyle=SUCCESS,values=('primary','secondary'))
combo.pack(side=LEFT, padx=5, pady=5)

d = tkb.DateEntry(root, bootstyle=INFO, dateformat='%Y-%m-%d')
d.pack(side=LEFT, padx=5, pady=5)

enter = tkb.Entry(root, bootstyle=INFO, textvariable="Enter Text", state="readonly")
enter.pack(side=LEFT, padx=5, pady=5)

frame = tkb.LabelFrame(root, bootstyle=SUCCESS, width=100, height=100, text="Test Frame")
frame.pack(side=LEFT, padx=50, pady=50)

tree = tkb.Treeview(root, bootstyle=SUCCESS, columns=("column1"), displaycolumns="column1")
tree.pack(side=LEFT, padx=5, pady=5)

meter = tkb.Meter(root, bootstyle=SUCCESS, interactive=True)
meter.pack(side=LEFT, padx=5, pady=5)


root.mainloop()

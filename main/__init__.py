from controller.Controller import Controller
from view.View import View
from model.Model import Model

m = Model()
view = View()
cont = Controller(m)
view.put_controller(cont)

view.run()




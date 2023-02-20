import controller as controller

from Controller import Controller
from Model import Model
from View import View


class Program:
    model = Model()
    controller = Controller(model)
    view = View(controller, model)

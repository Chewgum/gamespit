#!/usr/bin/python
# -*- coding: utf8 -*-

# Cu-Cu

# Author: Alfonso E.M. <alfonso@el-magnifico.org>
# License: Free (GPL2) 
# Version: 1.0 - 27/Feb/2013

import random

from Game import Game

class Menu(Game):

    def start(self):
        return

    def loop(self):

        while True:

          which=random.randint(1,14)

          self.fill()
          self.DISPLAY.print_image(self.IMAGES["door-open"])
          self.DISPLAY.print_image(self.IMAGES["face"+str(which)])
          self.DISPLAY.show()
          self.wait(1000)

          self.fill()
          self.DISPLAY.print_image(self.IMAGES["door-closed"])
          self.DISPLAY.show()

          input_type=self.CONTROLLER.wait_for_user_action()

          if input_type == "K": #Keyboard
              if self.CONTROLLER.key_name == "escape": #quit game
                    break 

          self.wait(5)


# Main
def main(name, CONF, DISPLAY, CONTROLLER):

    menu=Menu(name, CONF,DISPLAY,CONTROLLER)
    menu.start()
    menu.loop()


import kivy
kivy.require('1.0.9')

from kivy.uix.widget import Widget
from widget.ball import Ball
from kivy.properties import ObjectProperty, NumericProperty
from kivy.vector import Vector
from kivy.core.window import Window

class Game(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    angle = NumericProperty(0.)

    def update(self, dt):
        result = self.ball.update()
        if result is not None:
            if result:
                self.player1.score += 1
                self.ball.pos = (Window.width * .5 + Window.height * .25, Window.height * .5)
                self.ball.velocity = (0, 0)
            else:
                self.player2.score += 1
                self.ball.pos = (Window.width * .5 - Window.height * .25, Window.height * .5)
                self.ball.velocity = (0, 0)
            if (self.player1.score == 10) or (self.player2.score == 10):
                if self.parent != None:
                    self.parent.remove_widget(self)
        

        for player in self.player1, self.player2:
            if self.ball.collide_widget(player):
                self.angle = Vector(player.pos).angle(Vector(self.ball.pos))
                print self.angle
                self.ball.update_angle(self.angle)

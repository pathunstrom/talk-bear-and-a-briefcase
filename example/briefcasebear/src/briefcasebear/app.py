"""
A tiny video game.
"""
import ppb
from ppb.features import animation


class Player(ppb.Sprite):
    direction = ppb.directions.Right
    speed = 3
    image = animation.Animation('briefcasebear/resources/bear-walk-cycle{1..4}.png', 8)
    size = 2
    def on_update(self, event: ppb.events.Update, signal):
        self.position += self.direction * self.speed * event.time_delta


class BriefcaseBear(ppb.BaseScene):
    def on_scene_started(self, event, signal):

        self.add(Player())


def main():
    ppb.run(
        starting_scene=BriefcaseBear,
        title='Briefcase Bear',
    )

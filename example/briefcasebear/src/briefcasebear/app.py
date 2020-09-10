"""
A tiny video game.
"""
import ppb


class BriefcaseBear(ppb.BaseScene):
    def on_scene_started(self, event, signal):

        self.add(ppb.Sprite(
            image=ppb.Image('briefcasebear/resources/briefcasebear.png'),
        ))


def main():
    ppb.run(
        starting_scene=BriefcaseBear,
        title='Briefcase Bear',
    )

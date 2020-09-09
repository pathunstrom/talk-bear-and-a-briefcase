"""
A tiny video game.
"""
import ppb


class BriefcaseBear(ppb.BaseScene):
    def __init__(self, **props):
        super().__init__(**props)

        self.add(ppb.Sprite(
            image=ppb.Image('briefcasebear/resources/briefcasebear.png'),
        ))


def main():
    ppb.run(
        starting_scene=BriefcaseBear,
        title='Briefcase Bear',
    )

Now we can move on to that code inside our scene started handler:

self dot add ppb dot Sprite.

Sprites are ppb's name for game objects. They handle carrying metadata
for the various subsystems to operate one, specifically the renderer,
and also the data and event handlers required to simulate your game.

Right now, our sprite is just a standard sprite with no event handlers,
so we can fix that by making a Player class that subclasses Sprite.

We'll give it a direction vector and speed as class attributes, then in
an on_update handler we'll move the sprite a little in that direction
each frame.

Remember, each handler accepts an event parameter. The update event has
a time delta that we can include in the calculation!

Next we replace the basic sprite with our new sprite.

While we're here, I'm going to add a fun little animation for our
player.

Isn't he cute?

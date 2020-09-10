Next let's cover what scenes are, and how to use them.

A "scene" is just a part of a video game. It's a helpful way to split a
game into multiple parts. In ppb we often use them to differentiate
between things like splash screens, menus, and game levels.

Under the hood, ppb keeps them in a stack, and only the top of the stack
is allowed to respond to events. To demonstrate using events, let's
refactor this scene.

The initialization of this scene happens in dunder init, but that's not
the only place you can do scene initialization, and the other way has
some advantages.

By converting init to `on_scene_started` like so, we can now signal
events during scene initialization.

All events look like this: on event name, and accepts an event and a
signal function.

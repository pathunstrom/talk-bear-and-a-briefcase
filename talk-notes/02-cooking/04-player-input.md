The last thing you need to know before making your own game is the
techniques for player input. I've introduced you to the idea of events,
but this is where we really put those skills to use.

Player input on a computer comes from a couple of sources: keyboard and
mice most often. (Eventually, ppb will support touch events, but that
day is not today.) There are five different events that let you respond
to these inputs.

For a mouse, we have on_mouse_motion, on_button_pressed and
on_button_released. Each of these will have a position in the event
which tells you where the mouse is at the time of the event. It'll also
tell you which button was pressed with the ppb.buttons objects in button
or buttons depending on the event.

Keyboard events are on_key_pressed and on_key_released. They're much
simpler: They tell you which key was pressed from ppb.keycodes and which
modifiers are present.

Putting all of this together will take a long while. That fastest I've
managed to finish up a video game was 48 hours, and you shouldn't expect
your first game to be much faster than that. You should definitely time
box your efforts if what you want to do is practice game development.
Maybe give yourself a month!

In the meantime, here's a game I've already made.

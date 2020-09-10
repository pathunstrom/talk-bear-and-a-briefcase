Very briefly, the briefcase setup defined a dunder main file that calls
app.main, so our entry point is this file.

Inside, we find a collection of imports, a class called BriefcaseBear,
and a function called main.

Run has only a single code statement: A call to ppb dot run.

ppb.run is the helper function provided by ppb to help set up your game
engine and run it in a single step. The important thing to know is that
run takes all the same options as a GameEngine instance, and passes them
to the engine for you.

The briefcase cookie cutter gave use the two most important ones: the
starting scene, and a title.

At this point, we have a functioning program. If you run the command
briefcase dev, you'll get to see a preview of this very basic game.

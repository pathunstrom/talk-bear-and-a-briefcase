First, let's talk about organization:

Your briefcase app is a Python package. It lives in the src directory
under the app name directory. Inside the package, you've find a couple
of things already there. The one we're going to start with is resources.

For briefcase to know where your image and sound files live, you need to
put them in this directory. You'll notice that we already have a couple
of files here named after our project. These are beeware defaults, so
we're going to replace them.

You can make pngs with your favorite art programs, the other two I just
look up png converters to change the icon.

A note when we start adding to this directory: ppb's file lookup
requires each subdirectory to have a dunder init file, so make sure to
do so if you subdivide anything here.

With that warning out of the way, let's move on to app.py.

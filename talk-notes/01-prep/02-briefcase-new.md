(2.1)

Now with our preparation in order, it's time to get the scaffolding for
our game ready. Thankfully, briefcase can do that for us!

Let's start by running briefcase new in our shell. As you can see, we
get some output that will walk us through this. First, we need a formal
name. This is a name for humans, so write it as you want people to read
it. I'll call mine Briefcase Bear.

For the second entry, we need the name computers care about. It does
warn you that the name here _must_ be usable as a Python package
identifier. See PEP 508 for more detail.

We'll use the default briefcase gives use.

Now we need a Bundle Identifier, which is a short way of saying the
identifier for you. It's usually a domain name you control, but in
reverse order from how you're used to seeing it. So my website lives at
piper.thunstrom.dev so I'll use dev.thunstrom.piper.

Next, we need to name the project. I'm going to let it match the name of
the application, but you can have multiple apps in this single project
if you'd prefer.

(2.2)

Now briefcase needs some metadata about the project, starting with a
description. Let's say this project is a tiny video game.

Now the author, I'm Piper Thunstrom, but you should put your name, or
the team behind your game.

Now an email, which I use with all my games.

This is a url, you can change this later, so I'll leave this as is until
I set up a project page for it.

(2.3)

Finally, we need to pick a license. Pick your favorite, or add your own
with option 9: other.

In this case, I'll choose proprietary (or no license) until I decide how
I'd prefer to license my code.

We now get to pick a GUI framework. For today, pick PursuedPyBear, but
there's 2 other built in ones, or you can default to None to add your
own.

A little bit of output later, and we have a briefcasebear in our project
directory.

(Add more to this.)
(1.1)

I am Piper Thunstrom. By day I'm a senior software engineer who makes a
living doing web development.

By night, though, I work hard to make programming increasingly
accessible to a wider and wider audience. I've helped run local Python
user groups and volunteered for various roles at a couple of
conferences.

I do regular speaking engagements where I can be found
going on at length about some of my favorite technical topics, like game
dev, and the amazing power hidden in the corners of the Python standard
library. Or I might talk about harder topics, like coming out trans when
you're well known in your community.

I'm also a game developer and have focused a significant portion of my
career on sharing my love for games with others.

So today, I'm going to share a new recipe that has revealed a new Python
superpower: We're putting a bear in a briefcase by building a game with
PursuedPyBear and packaging it up for end users using Beeware's
Briefcase.

(1.2)

So let's start with PursuedPyBear. an education-focused game library
that I am the author and co-maintainer of. For brevity, I'll refer to it
as ppb for the rest of this talk.

ppb started its life as an ill-conceived MVC framework, complete with
strong separation of concerns and dependency injection. It didn't take
me long to realize that I was going down the wrong path when I
completely failed to make a game using it only six months after the
project started.

About the time I was ready to throw it out, I got a lot of requests to
focus on a game making tool specifically for CS education. That started
by doing a lot of research on API design, and rebuilding ppb to run the
API I wanted, instead of the software purity I had tried to design with
previously.

Now, we focus on a principles driven development, with a focus on
students and learners first, unleashing creativity without limitations
baked into the platform, a genuinely fun API, and a strong focus on
inclusion.

(1.3)

Second, we need to cover BeeWare and Briefcase. BeeWare's focus is
expanding the boundaries of Python: write one code base, deploy it
everywhere. By everywhere, they say in their header: iOS, Android,
Windows, MacOS, Linux, Web, and tvOS.

This includes a bunch of neat tools and libraries that allow you to do
things Python just wasn't very good at before. Things like Toga, which
allows you to write GUIs that use the OS styled widgets in Python.

Today, though, we care about Briefcase: A packaging tool for Python
applications. If you've heard of Py2App or PyInstaller, you've got the
right idea of what briefcase does.

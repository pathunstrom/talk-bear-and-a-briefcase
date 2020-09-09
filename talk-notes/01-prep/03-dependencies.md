One of the neat things about briefcase is that it uses the new world of
packaging configuration: pyproject.toml. Unfortunately for us, it fills
this out based on a fixed version of ppb, so we're going to need to open
this file and modify the metadata. Pay attention, because if you need to
make changes later (like the web page for your project) this is where
you'll need to do it.

Let's open pyproject.toml.

At the top is briefcase metadata. This is things like the name of the
project, your information, and the licensing info.

Below that is the actual information we care about: This is information
about the application we're building, including the requirements. See
where it says ppb 0.8? Let's bump that version up to the latest: ppb
0.10.

That gets us ready for starting on our new game!
With our game working, it's time to to prep it for our audience. That
means packaging, testing, and uploading your game. We'll start by
building our first package.

To start, go into your project and run briefcase create. A note here:
Right now, you can mostly only build a package on the platform you're
building for, especially for PC platforms. Most of these examples are
based on Windows, so keep that in mind as we move on.

After running this command, we now have a windows directory in our app
directory. Right now, it's just the files and metadata we'll be building
into the final installer.

You can explore the files and find your app, copies of all of your
resources, and also a lot of additional python site packages.

A current issue of Briefcase is that it has to port all of your
dependencies _and_ all of the standard library. Honestly this is still
tiny as a lot of games go, but if you're concerned about the size of
your installers, this is a thing to note.

Once you're satisfied that you've got everything in order, time to build
the installer.

briefcase package will build our installer!

Now if we look in our package, we see a BriefcaseBear-0.0.1.msi. This is
a full featured windows installer!

Because software can often go wrong, before we move on to using this
installer, I want to point out a few tips for making updates to this
package. First, modify the code you'd like to change. Add any new
resources.

Then, open up the pyproject.toml again. In the top section, you should
bump the version number.

After that, we run briefcase update.

Now, we can repackage our game and get a new version installer. This
will be important if you patch a game after release.

Go us!

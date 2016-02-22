invoke-hello-world
==================
This example shows how to use [invoke](http://www.pyinvoke.org/) as a CLI.
Instead of having to type `invoke command`, it turns the tasks file into an
executable script and automatically brings up help messages when they make
sense. It also automatically loads the json configuration file with the name
of your script instead of 'invoke.json'.

In this example, my script is "hello.py":

 * `./hello.py` lists all of the available tasks
 * `./hello.py --help` also lists all of the available tasks
 * `./hello.py --help hello` shows the docstring for the 'hello' task
 * `./hello.py hello` runs the hello task
 * `./hello.py hello --message "Konnichiwa sekai"` runs the task setting the message parameter

To do this the old fashioned way, you would name "hello.py" to "tasks.py" and do the following:

 * `invoke --list`
 * `invoke --list`
 * `invoke --help hello`
 * `invoke hello`
 * `invoke hello --message "Konnichiwa sekai"`

This is cool because it allows you to create a more natural wrapper around your program.

Future Work
-----------
Make it possible to install the package and work correctly.

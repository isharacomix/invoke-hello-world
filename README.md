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
 * `./hello.py --help hello` shows the docstring for the 'hello' taks.

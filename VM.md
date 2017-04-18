Using the VM
============

Once you have installed the VM following the instructions in 
[PREREQUISITES.md](PREREQUISITES.md) (option 1) you are ready to begin using
the tutorial tools!

Starting
--------

You can check the status of the VM by running `vagrant status` from within 
the repo directory. If it is not already running, start it with
`vagrant up --provider virtualbox`.

Logging In
----------

You can log in to the VM using `vagrant ssh` on the command line or by
connecting to `localhost:2222` via ssh.

Swagger Editor
--------------

Two versions of the web-based [swagger-editor](https://github.com/swagger-api/swagger-editor)
have been installed on the VM and should be accessible from the host machine. 

http://localhost:8000/ - Swagger Editor 2.x (includes links to code generation service)
http://localhost:8001/ - Swagger Editor 3.x (improved editor but no coge generation) 

Python API Implementation
-------------------------

An example implementation using [Connexion](https://connexion.readthedocs.io/en/latest/)
is included in the tutorial repo. To run it you first need to activate the
Python virtual environment (using the `workon` command provided via
virtualenvwrapper.):

```
workon tutorial
```

Then to run the connexion app:

```
python -m betterapis
```

With the application running, the API and Swagger UI are available from the 
host machine.

The API should be available here:

http://localhost:8080/talks

The Swagger UI for the API is available here:

http://localhost:8080/ui/

Swagger Validator
-----------------

A validation tool has been installed. This will help you find errors in working
specification files. For example, you can run it on one of the tutorial solution
files:

```
swagger validate tutorial-repo/lessons/lesson-1.02/solution.yaml
Results: 0 errors, 0 warnings
```

Dredd
-----

The [Dredd](http://dredd.readthedocs.io/en/latest/) testing tool is installed.
You may verify it works and see usage information by running:

```
dredd --help
```

Swagger-codegen
---------------

In addition to being available via links in the Swagger Editor 2.x,
swagger-codegen is available on the command line in the VM. For usage
information run:

```
java -jar swagger-codegen.jar help
```


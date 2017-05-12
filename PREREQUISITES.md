Prerequisites
=============

In order to follow-along with the exercises in this tutorial you will need 
to install some applications and tooling. Installation can take a while so
please try to make sure everything is installed before the session.

*If you prefer not to install all of the tooling individually you should use
Option 1. If you are comfortable with installing npm packages and setting
up a Python 3.4+ virtualenv then use Option 2 below.*


Option 1: Vagrant + VirtualBox
------------------------------

We have created a VM with all of the required applications already installed
and configured. To use it you will need to have Vagrant and Virtualbox
installed.

- [Download & Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Download & Install Vagrant](https://www.vagrantup.com/docs/installation/)

*Be sure to reboot your host system after installing Vagrant + VirtualBox.*

Once they're installed and you've rebooted, clone this repo:

```
git clone https://github.com/tylerdave/OpenAPI-Tutorial.git
cd OpenAPI-Tutorial
```

Then from within the repo dir, start the Vagrant VM:

```
vagrant up --provider virtualbox
```

Then connect via ssh:

```
vagrant ssh
```

**On Windows?** You will need to either install and configure Git Bash or SSH
to localhost:2222 using an SSH clinet program. More details:

- Connect via PuTTY: http://stackoverflow.com/a/9924122/
- SSH with Git Bash: http://stackoverflow.com/a/16247703/

### Using the VM

See [VM.md](VM.md) for more usage information.

Option 2: Manual Installation
-----------------------------

If you prefer to install all the tools into your own development environment,
you may install the following:

### Applications

- Node.js and npm
- Python 3.4+

### Node Packages

Install the following Node.js packages using `npm`:

- dredd
- swagger

```
npm install -g dredd swagger
```

Note: You can omit the `-g` flag if you wish to install the packages for only
the current user.

### Tutorial Repo

Once those are installed, clone this repository:

```
git clone https://github.com/tylerdave/OpenAPI-Tutorial.git tutorial-repo
```

### Python Environment

Create and activate a new Python virtualenv:

```
python -m venv tutorial
source tutorial/bin/activate
```

With the `tutorial` virtualenv active, Install the implementation package and
its dependencies:

```
pip install -e implementation
```

### Swagger / OpenAPI Editor

If you used Option 1, a copy of the Swagger Editor is included in the VM. If
you chose Option 2 then you should either:

- Use the online editor here: http://editor2.swagger.io/
- Install it locally: https://github.com/swagger-api/swagger-editor/tree/2.x#running-locally

*Note: For now we recommend using the 2.x version of the editor as the 3.x 
version currently has some issues refreshing the validator.*

Also Recommended
----------------

In order to test the API implementation locally, you should have a tool for 
making HTTP requests. You are free to use any tool you are comfortable with. We
recommend Postman for this purpose if you don't have a strong preference.

### Postman

Postman can be installed as a native application or a Chrome plugin.

Get Postman here: [Download Postman](https://www.getpostman.com/)

If this is your first time using Postman, we recommend using these guides in
order to get familiar with the tool:

- [requests](https://www.getpostman.com/docs/requests)
- [collections](https://www.getpostman.com/docs/collections)

Some of the tutorial lesson directories contain a file named 
`postman_collection`. These will help you complete the exercises more quickly.

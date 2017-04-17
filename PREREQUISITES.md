Prerequisites
=============

In order to follow-along with the exercises in this tutorial you will need 
to install some applications and tooling. Installation can take a while so
please try to make sure everything is installed before the session.

Option 1: Vagrant + VirtualBox
------------------------------

We have created a VM with all of the required applications already installed
and configured. To use it you will need to install Vagrant and Virtualbox.

- [Download & Install Vagrant](https://www.vagrantup.com/docs/installation/)
- [Download & Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)

Once they're installed, make a new directory for your work and cd to it. For example:

```
mkdir openapi-tutorial
cd openaoi-tutorial
```

Then clone this repo into a subdirectory named `tutorial-repo`:

```
git clone https://github.com/tylerdave/OpenAPI-Tutorial.git tutorial-repo
```

Then initialize and start a new Vagrant VM:

```
vagrant init [BOX COMING SOON]
vagrant up --provider virtualbox
```

Then connect via ssh:

```
vagrant ssh
```

Option 2: Manual Installation
-----------------------------

If you prefer to install all the tools into your own development environment,
you may install the following:

### Applications

- Java Runtime (7 or 8)
- Node.js and npm
- Python 3.4+

### Node Packages

Then install the following Node.js packages using `npm`:

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
./tutorial/bin/activate
```

Install the implementation package and its dependencies:

```
pip install -e tutorial-repo/implementation/betterapis
```

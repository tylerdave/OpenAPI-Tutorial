This Presentation
=================

This directory contains a Remark.js HTML presentation file and the input files
used to generate it.

Files
-----

- slides.md: Markdown slide contents
- style.css: Presentation stylesheet
- presentation.html: Generated presentation file

Remarker
--------

[Remarker](https://github.com/tylerdave/remarker) is used to generate the 
presentation based on the input files. It can be installed in a Python 2 or 3
virtualenv or via [pipsi](https://github.com/mitsuhiko/pipsi).

Generating
----------

To generate an updated copy of the presentation, first make your changes to the
input files as needed and then run:

`remarker -o presentation.html --css-file style.css -t "OpenAPI Tutorial" slides.md`

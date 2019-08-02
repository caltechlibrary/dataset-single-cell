Dataset single cell
=================================================

This is a demonstration of using dataset to organize single cell data


Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Known issues and limitations](#known-issues-and-limitations)
* [Authors and history](#authors-and-history)

Introduction
------------


Installation
------------

Clone this repo or fownload the zip from GitHub using the green button. You need to have Python 3 on your machine
([Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a great installation option). 

Install the dataset dependency by typing `pip install py_dataset`

You need to get a `credentials.json` file for your Google account.  Go to
https://developers.google.com/sheets/api/quickstart/go and click the blue
button.  Make up a project name (it doesn't matter). Click the blue button 
labeled Download Client Configuration, which will download a credentials.json
file. Currently, you need to move the file from your downloads folder to your 
current working directory (e.g. on my Mac I did mv ~/Downloads/credentials.json . )

If you want to look at the dataset collection on the command line, download the
[dataset](https://github.com/caltechlibrary/dataset) binaries.  We compile them
for most platforms (including Raspbian).

Usage
-----

Type `python dataset-single-cell.py`.  This will read metadata from the google
sheet, build a collection, run through mock data processing, and demonstrate
two approaches for returning a subset of results.


Known issues and limitations
----------------------------

Should split multi-value fields from spreadsheet into arrays.

Are there better ways of getting the kallisto files for downstream analysis
(such as file streams from within the collection)?

Authors and history
---------------------------

Tom Morrell, Caltech Library


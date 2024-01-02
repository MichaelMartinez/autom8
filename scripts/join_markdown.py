# This script will walk a directory and join all the markdown files into one
# file. It will also add a header to each file with the filename and a link to
# the next file.
# This script will be interactive and ask for the directory to walk and the
# output file name.
# This script will also ask if you want to add a header to each file.
# This script will also ask if you want to add a footer to each file.
# This script will also ask if you want to strip markdown formatting from the
# output file.


import os
import sys
import re
import glob
import argparse
import shutil
import time
import datetime
import subprocess
import platform
import logging
import logging.handlers
import json
import requests
import urllib
import urllib2

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.handlers.RotatingFileHandler(
    'join_markdown.log', maxBytes=1000000, backupCount=5)
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)

# Set up the command line arguments
parser = argparse.ArgumentParser(
    description='Join all the markdown files in a directory into one file.')
parser.add_argument('-d', '--directory',
                    help='The directory to walk.', required=True)
parser.add_argument(
    '-o', '--output', help='The output file name.', required=True)
parser.add_argument(
    '-f', '--footer', help='The footer file name.', required=False)
parser.add_argument('-s', '--strip', help='Strip markdown formatting from the output file.',
                    required=False, action='store_true')
parser.add_argument('-v', '--verbose', help='Verbose output.',
                    required=False, action='store_true')
args = parser.parse_args()

# Set up the variables
directory = args.directory
output = args.output
footer = args.footer
strip = args.strip
verbose = args.verbose

# Set up the variables
directory = args.directory
output = args.output
footer = args.footer
strip = args.strip
verbose = args.verbose

#

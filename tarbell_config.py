# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "fellowship"

# Descriptive title of project
TITLE = "CCSO Fellowship"

# Google spreadsheet key
SPREADSHEET_KEY = "1_PY8wVy5y11HdP9TLIjczIp7lLF3XdVnH4vkHhqFooI"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "portfolio.sarahemuraray.com/fellowship",
    "staging": "staging.sarahemurray.com/fellowship",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'fellowship',
    'title': 'CCSO Fellowship'
}
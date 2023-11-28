# Documentation

The code is written in Python and works with the usage
Flask and request modules.

The request module is used to handle requests coming from the client
while Flask is used to generate a response from the data received
with the help of Jinja templates. 

## Requirements
All the required module are listed in the file `requirements.txt`
and can be installed thought pip with the following command:
``` shell
pip install -r requirements.txt
```

## Usage
Start the program with `python.exe APOD_viewer.py` in the terminal,
it will start a development server at http://127.0.0.1:5000.

By default it shows today's picture with it's date and title at the top
and the copyright, if present, with it explanation at the bottom.

the image can be clicked to access an high quality version, if present,
allowing zoom in and see details thanks to the browser in-built
image viewer.

At the top of the page fields are present to make a custom query,<br>
the first is a list of query types:
- **Date**, the default, allows to select a date and query for that
date picture.
- **Date range**, allows to select a start and an end date to query for
pictures in a date range.
- **Random images**, allows to choose a number, the amount if pictures
and query for a list of random pictures.

Each query type will change the rendered fields to fit it needs.

Both the **Date** date filed and the **Date range** start date field
are limited to start from 16 June 1995 and end with today's date, as
it is the APOD API allowed range.<br>
The **Date range** end date field is limited to start from the start date
value and end with today's date and will change to the start date value,
if it's previous to the start date, this is done to avoid invalid
queries.<br>
The **Random images** number field is limited to start from 1 and end
at 100, as it is the APOD API allowed range. 

If the query contains more than one picture, a grid view will be used,
this can happen only if using the **Date range** and the
**Random images** queries.

Despite being the **Astronomy Picture Of the Day** viewer videos can be
found in queries which are correctly rendered in the page.

In the absence of a video or a picture a default image is used:

<img src="static/default.png" alt="default.png" width="256">
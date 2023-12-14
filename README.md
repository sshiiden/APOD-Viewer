# APOD Viewer
query data from the [apod](https://apod.nasa.gov) API and visualizes it.

- [Requirements](#requirements)
- [Usage](#usage)
  - [Viewer](#viewer)
  - [XML Gateway](#xml-gateway)
- [Code](#code)
## Requirements
All the required modules are listed in the `requirements.txt` file
and can be installed thought pip with the following command:
``` shell
pip install -r requirements.txt
```
## Usage
### Viewer
Start the program with `python APOD_viewer.py` in the terminal,
it will start a development server at http://127.0.0.1:5000.

For the XML version use `python APOD_viewer_XML.py`,
the default server address is http://127.0.0.1:5002, it requires
the [XML Gateway](#xml-gateway) to be running.

By default it will show today's picture with it's date and title at the top
and the copyright, if present, with an explanation at the bottom.

the image can be clicked to see an high quality version, if present,
allowing zoom in and see details thought the browser in-built
image viewer.

At the top of the page a form is present to make a custom query,<br>
the first is a list of query types:
- **Date**, the default, allows to select a date and query for that
date's picture.
- **Date range**, allows to select a start and an end date to query for
pictures in a range.
- **Random images**, allows to choose the amount of pictures and query
for a list of random pictures.

Each query type will change the rendered fields as needed.

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

### XML Gateway
Start the program with `python XML_gateway.py` in the terminal,
the default server addres is http://127.0.0.1:5001.

The allowed arguments are:
- **date**: a date to query for.
- **start_date**: the start of a date range, cannot be used
with `date`.
- **end_date**: end of a date range when used with `start_date`
default to today's date.
- **count**: an integer from 1 to 100, returns `count` random
images, cannot be used with any of the above. 

Example query: `http://127.0.0.1:5001?count=3`
# Documentation
- [Requirements](#requirements)
- [Usage](#usage)
- [Code](#code)
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

## Code
The code is written in python and works with the usage of the flask and
the request modules.<br>
The request module is used to handle requests coming from the client
while flask is used to generate a html from the data received with the
help of Jinja templates.

The python code is found in `APOD_viewer.py`, while all the jinja
templates are found in the `templates` directory.<br>
In the `static` directory can be found:
- an image, named `default.png`, used when a picture is missing
- a javascript file, named `script.js`, to allow to change the
query type
- a css file, named `styles.css`, to make everything viewable

### Python
#### getData()
Takes care of getting data from the form and getting the pictures to
be displayed.

Returns a tuple , `(images: List[Dict], data: Dict)`

`images` is a list of dictionaries, returned by the query, rappresenting 
the pictures to be displayed with their data.
```python
images = requests.get(url).json()
```
`data` is a dictionary containing data useful to the page
```python
data = {"filter_type": "single",
        "start_date": today,
        "end_date": today,
        "n_images": 1,
        "today": today}
```
#### index()
Calls `getData` to get the data needed by the `base.jinja` template
and returns the html page.
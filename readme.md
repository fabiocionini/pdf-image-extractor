# PDF Image Extractor
[fabiocionini.it](https://fabiocionini.it)

Quick and dirty PDF image extractor script.

## Installation
- Create a virtual environment, such as `python3 -m venv venv; source venv/bin/activate`
- Install requirements with `pip install -r requirements.txt`

## Usage
Run with `python pdf_image_extractor.py [filename.pdf]`. 

Image files will be automatically extracted and saved in a folder named from the PDF file using the format `[pdf_filename]_page[page_number]_image[image_number].[image_ext]`.

## Known Issues
- Does not support CMYK colorspaces
- Complains if the target folder already exists

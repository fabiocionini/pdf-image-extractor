import os
import sys
from pikepdf import Pdf, PdfImage

if len(sys.argv) != 2:
    sys.exit("Usage: python pdf_image_extractor.py [filename.pdf]")

filename = sys.argv[1]
file = Pdf.open(filename)

if file:
    file_prefix = filename.rsplit('.', 1)[0]
    os.mkdir(file_prefix)
    for page_count, page in enumerate(file.pages):
        image_keys = list(page.images.keys())
        for img_count, image_key in enumerate(image_keys):
            raw_image = page.images[image_key]
            pdf_image = PdfImage(raw_image)
            image_name = '{0}/{1}_page_{2}_image_{3}'.format(file_prefix, file_prefix, str(page_count + 1).zfill(2), str(img_count + 1).zfill(2))
            pdf_image.extract_to(fileprefix=image_name)



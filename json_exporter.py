# json_exporter2.py

# importing required modules
import json
import os

from pypdf_text_generator import extract_text_by_page


def export_as_json(pdf_path, json_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    data = {'Filename': filename}
    data['Pages'] = []
    
    counter = 1
    for page in extract_text_by_page(pdf_path):
        text = page
        print(text)
        page = {'Page_{}'.format(counter):text}
        data['Pages'].append(page)
        counter += 1
    
    with open(json_path, 'w') as fh:
        json.dump(data, fh)

if __name__ == '__main__':
    pdf_path = 'Test for json (2) (1).pdf'
    json_path = 'Test for json (2) (2).json'
    export_as_json(pdf_path, json_path)

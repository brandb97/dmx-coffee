#utf-8

from html.parser import HTMLParser
import os.path
import shutil

class imgHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.output = []
 
    def handle_starttag(self, tag, attrs):
        self.output.append(f'<{tag}')
        for name, value in attrs:
            if tag == 'img' and name == 'src':
                if len(value.split('/')) != 1:
                    value = '\\'.join(value.split('/'))[1:]
                    value = os.path.join('D:\\StudyProgram\\咖啡', value)
                new_value = os.path.basename(value)
                self.output.append(f' {name}="{new_value}"')
                shutil.copy(value, new_value)
            else:
                self.output.append(f' {name}="{value}"')
        self.output.append('>')
 
    def handle_endtag(self, tag):
        self.output.append(f'</{tag}>')
 
    def handle_data(self, data):
        if self.output:
            self.output.append(data)
 
    def handle_comment(self, data):
        self.output.append(f'<!--{data}-->')
 
    def handle_entityref(self, name):
        self.output.append(f'&{name};')
 
    def handle_charref(self, name):
        self.output.append(f'&#{name};')
 
    def output_content(self):
        return ''.join(self.output)

import chardet
 
with open('index.html', 'rb') as f:
    raw_data = f.read()
    encoding = chardet.detect(raw_data)['encoding']

with open('index.html', 'r', encoding=encoding, errors='ignore') as f:
    parser = imgHTMLParser()
    parser.feed(f.read())


with open('index.html', 'w', encoding=encoding, errors='ignore') as f:
    f.write(parser.output_content())
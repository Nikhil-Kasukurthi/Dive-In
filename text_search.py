import tornado.ioloop
import tornado.web
import json
from wikiapi import WikiApi
# Google Cloud vision API
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import base64

client = vision.ImageAnnotatorClient()

wiki = WikiApi()

class TextSearchHandler(tornado.web.RequestHandler):
    """
        Route for getting a list of possible Wikipedia articles.
    """

    def post(self):
        extracted_text = self.get_argument('text')
        possible_articles = wiki.find(extracted_text)
        results = {}
        results['Possible Articles'] = possible_articles
        self.write(json.dumps(results))


class TextSearchImagesHandler(tornado.web.RequestHandler):
    """
        Route for getting list of possible Wikipedia articles
        along with images of each article. 
    """
    def post(self):
        extracted_text = self.get_argument('text')
        possible_articles = wiki.find(extracted_text)
        results = {}
        results['Possible Articles'] = []
        for article_id in possible_articles:
            if len(article_id) > 20:
                continue
            result = {}
            article = wiki.get_article(article_id)
            #image_array = article.images
            result["article_id"] = article_id
            result["image"] = article.image
            result["summary"] = article.summary
            print(result)
            results['Possible Articles'].append(result)
        self.write(json.dumps(results))


class SummaryHandler(tornado.web.RequestHandler):
    """
        Route for getting summary of requested article.
    """
    def post(self):
        article_id = self.get_argument('article_id')
        article = wiki.page(article_id)
        summary = article.summary
        results = {}
        results['Results'] = summary
        self.write(json.dumps(results))

class UploadHandler(tornado.web.RequestHandler):

    def post(self):
        file = self.request.files['file'][0]
        content = file['body']
        image = types.Image(content=content)     

        response = client.text_detection(image=image)
        texts = response.text_annotations
        
        JSON = {}
        JSON['results'] = []
        for text in texts:
            resultJSON = {}
            resultJSON['description'] = text.description
        	# print('\n"{}"'.format(text.description))
            vertices = (['({},{})'.format(vertex.x, vertex.y)
		                for vertex in text.bounding_poly.vertices])
        	# print('bounds: {}'.format(','.join(vertices)))
            resultJSON['bounds'] = vertices
            JSON['results'].append(resultJSON)
        
        self.write(JSON)

def make_app():
    return tornado.web.Application([
        (r"/search", TextSearchHandler),
        (r"/searchImage", TextSearchImagesHandler),
        (r"/summary", SummaryHandler),
        (r"/upload", UploadHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

import tornado.ioloop
import tornado.web
import json
from wikiapi import WikiApi

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


def make_app():
    return tornado.web.Application([
        (r"/search", TextSearchHandler),
        (r"/searchImage", TextSearchImagesHandler),
        (r"/summary", SummaryHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

import tornado.ioloop
import tornado.web
import wikipedia as wiki
import json


class TextSearchHandler(tornado.web.RequestHandler):
    """
        Route for getting a list of possible Wikipedia articles.
    """

    def post(self):
        extracted_text = self.get_argument('text')
        possible_articles = wiki.search(extracted_text)
        results = {}
        results['possible_articles'] = possible_articles
        self.write(json.dumps(results))


class TextSearchImagesHandler(tornado.web.RequestHandler):
    """
        Route for getting list of possible Wikipedia articles
        along with images of each article. 
    """
    def post(self):
        extracted_text = self.get_argument('text')
        possible_articles = wiki.search(extracted_text)
        results = {}
        results['possible_articles'] = []
        for article_id in possible_articles:
            if len(article_id) > 20:
                continue
            result = {}
            article = wiki.page(article_id)
            image_array = article.images
            result["article_id"] = article_id
            result["images"] = image_array
            print(result)
            results['possible_articles'].append(result)
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

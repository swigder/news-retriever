# news-retriever

To run:
1. Install the event registry python package.  For example: `pip3 install eventregistry`
1. Run with your API key as an argument.  For example `python3 src/download.py YOUR-API-KEY-HERE`
1. The data will be under the `data` folder.
1. To control the list of articles you get back, modify the `get_article_list` method.  Details of the API can be found at <https://github.com/EventRegistry/event-registry-python/wiki>.

Note: You can get up to 10k articles with one run. This can take a few minutes; to only retrieve a smaller number of articles, pass only a subset of `uris` to `get_articles` in the main function.
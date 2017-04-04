from eventregistry import EventRegistry, QueryArticles, datetime, RequestArticlesInfo, ReturnInfo, ArticleInfoFlags, \
    RequestArticlesUriList, QueryArticle, RequestArticleInfo
import sys


def get_article_list(er):
    q = QueryArticles(lang='eng', categoryUri='dmoz/News', ignoreSourceUri='www.reuters.com')
    q.addRequestedResult(RequestArticlesUriList())
    return er.execQuery(q)


def get_articles(er, uris):
    q = QueryArticle(uris)
    q.addRequestedResult(RequestArticleInfo())
    return er.execQuery(q)


if __name__ == '__main__':
    er = EventRegistry(apiKey='')
    uris = get_article_list(er)
    articles = get_articles(er, uris['uriList']['results'][:200])
    for id, article in articles.items():
        print('title:', article['info']['title'])
        print('body:', article['info']['body'])
        print('\n')

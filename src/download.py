from eventregistry import EventRegistry, QueryArticles, datetime, RequestArticlesInfo, ReturnInfo, ArticleInfoFlags, \
    RequestArticlesUriList, QueryArticle, RequestArticleInfo
import sys
import json


def get_article_list(er):
    q = QueryArticles(lang='eng', categoryUri='dmoz/News',
                      ignoreSourceUri='www.reuters.com',  # we can't get reuters body
                      isDuplicateFilter='skipDuplicates')
    q.addRequestedResult(RequestArticlesUriList())
    return er.execQuery(q)['uriList']['results']


def get_articles(er, uris):
    articles = dict()
    for uri_group in chunk(uris, 200):
        q = QueryArticle(uri_group)
        q.addRequestedResult(RequestArticleInfo())
        articles.update(er.execQuery(q))
    return articles


def chunk(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


if __name__ == '__main__':
    er = EventRegistry(apiKey=sys.argv[1])
    uris = get_article_list(er)
    articles = get_articles(er, uris)
    with open('../data/data-10000.json', 'w') as fp:
        json.dump(articles, fp, indent=4)

import urllib.request, json
from operator import itemgetter


def topArticles(username, limit):
    # Write your code here
    with urllib.request.urlopen("https://jsonmock.hackerrank.com/api/articles?author=" + username + "&page=" + str(
            limit)) as url:
        data = json.loads(url.read().decode())
        items = data['data']
        items_re = []

        for p in items:
            if p['title'] == None and p['story_title'] == None:
                pass
            else:
                if p['title'] != None:
                    if p['num_comments'] == None:
                        num_comments = 0
                    else:
                        num_comments = p['num_comments']

                        items_re.append({'title': p['title'], 'num_comments': num_comments})
                else:
                    if p['num_comments'] == None:
                        num_comments = 0
                    else:
                        num_comments = p['num_comments']
                        items_re.append({'title': p['story_title'], 'num_comments': num_comments})
        sorted(items_re, key=lambda i: i['num_comments'], reverse=True)
        print(items_re[0]['title'])


result = topArticles('olalonde', 1)

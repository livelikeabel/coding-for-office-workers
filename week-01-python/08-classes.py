#클래스 class

#### Article variables
# title1 = "개발"


class Article:
    title = "dog foot"
    author = "abel"
    content ="dog foot is easy"
    view_count = 0

article1 = Article()
print(article1.title)

#### Article class with __init__
class Article2:
    author = "abel"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article2 = Article2("개발", "개발은 쉬워요")
article3 = Article2("코칭", "코칭은 쉬워요")
article4 = Article2("요리", "요리는 쉬워요")

"""
print(article2.title, article2.content)
print(article2.view_count)
article2.read()
print(article2.view_count)
"""




#### Article class inheritance 상속
class BrunchArticle(Article2):
    source = "브런치"

    def read(self):
        self.view_count = self.view_count + 2

brunch_article = BrunchArticle("개발", "개발은 쉬워요")
print(brunch_article.title)
print(brunch_article.content)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)

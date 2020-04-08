import re
import typing
from datetime import datetime

ALL_EVENTS: typing.List["Event"] = []


def parse_date(date_string: str) -> datetime:
  """
  Convert a date_string like '2020-01-01' into a datetime.
  """
  regex = re.compile(r'([0-9]{4})-([0-9]{2})-([0-9]{2})')
  result = regex.search(date_string)
  if not result:
    raise Exception(f"The date '{date_string}' is not in the right format.")
  year_string, month_string, day_string = result.groups()

  return datetime(int(year_string), int(month_string), int(day_string))


class Source:
  title = None
  """
  The verbatim title of this news article at the URL.
  """

  publication = None
  """
  The name of the publication, e.g. "The New York Times" or "The Wall Street Journal".
  """

  published: datetime = None
  """
  The date the article was originally published, e.g "2020-01-01".
  """

  url = None
  """
  The full URL of the news article, e.g. "https://www.nytimes.com/2020/04/06/world/coronavirus-live-news-updates.html"
  """

  pdf = None
  """
  The local path to a PDF copy of the same article, e.g. "./sources/2018-05-10-washington-post-top-white-house.pdf"
  
  The copy is insurance against broken URL's, article content changing, etc.
  """

  def __init__(self, title=None, publication=None, published=None, url=None, article_copy=None):
    self.title = title
    self.publication = publication
    self.published = parse_date(published)
    self.url = url
    self.pdf = article_copy


class Person:
  def __init__(self):
    pass


class Event:
  date: datetime = None
  """
  The date of the event.
  """

  title = None
  """
  A short, single-sentence summary of who did what.
  """

  description = None
  """
  A longer description of what happened, focusing on why it was Trump's fault and how it made things worse.
  """

  people = None
  """
  A list of people involved. For now, last names are good enough.
  """

  sources = None
  """
  A list of sources which confirm the information in the title and description.
  """

  def __init__(self, date=None, title=None, people=None, sources=None, description=None):
    self.date = date
    self.title = title
    self.people = people
    self.sources = sources
    self.description = description

    ALL_EVENTS.append(self)

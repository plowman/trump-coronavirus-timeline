import json
import os
import re
import subprocess

import iso8601
import pytz as pytz
import requests
from bs4 import BeautifulSoup

from scripts.shared import SOURCES_FOLDER


def run_cmd(shell_args, **kwargs):
  if isinstance(shell_args, list):
    shell_args = " ".join(shell_args)

  try:
    shell_response = subprocess.check_output(shell_args, shell=True, **kwargs)
    return str(shell_response, 'utf-8').strip()
  except subprocess.CalledProcessError as error:
    print(f"{error.output}\nError running cmd={error.cmd}. returncode={error.returncode}\n")
    raise error


def save_url_as_pdf(url, publication, title, published):
  """
  Save the given URL as a PDF in the appropriate location.

  :param url: The URL to save
  :param publication: The name of the publication, e.g. "The New York Times"
  :param title: The title of this article
  :param published: The date this was published, e.g. "2020-01-01"
  :return: The name of this PDF file in the sources folder.
  """
  title = title.lower()
  title = re.sub(r"[^a-z ]+", "", title)
  title = title.replace(" ", "-")
  publication = publication.lower().replace(" ", "-")
  pdf_path = f"{published}-{publication}-{title}.pdf"
  output_path = os.path.join(SOURCES_FOLDER, pdf_path)

  print(f"Saving url to path {output_path}")
  cmd = [
    "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome",
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={output_path}",
    url,
  ]
  run_cmd(cmd)

  return pdf_path


def get_metadata(url):
  """
  Get the metadata title, for example:
  <meta data-rh="true" property="og:title" content="White House Blocks C.D.C. Guidance Over ..."/>
  """
  content = requests.get(url).content
  soup = BeautifulSoup(content, features="html.parser")
  json_metadata = soup.find("script", attrs={"type": "application/ld+json"})
  if json_metadata:
    json_metadata = json.loads(json_metadata.string)
  else:
    print("WHOOPS no metadata for that URL.")
    json_metadata = {
      "datePublished": "1900-01-01",
      "isPartOf": {"name": "Unknown Publication"},
      "headline": "Unknown Headline",
    }

  for k, v in json_metadata.items():
    print(f"{k}: {v}")

  published = json_metadata.get("datePublished")
  if not published:
    raise Exception(f"No published in metadata: {json_metadata}")
  published = iso8601.parse_date(published)
  published = published.astimezone(pytz.timezone("America/New_York"))
  print(f"published: {published}")

  publication = json_metadata.get("isPartOf", {}).get("name")
  if not publication:
    publication = json_metadata.get("publisher", {}).get("name")
    if not publication:
      raise Exception(f"No publication in metadata: {json_metadata}")
  print(f"publisher: {publication}")

  title = json_metadata.get("headline")
  if not title:
    raise Exception(f"No title in metadata: {title}")
  print(f"title: {title}")

  return {
    "published": published,
    "title": title,
    "publication": publication
  }


def initialize_event(url):
  """
  Create the Source for an Event at the given url
  """
  metadata = get_metadata(url)
  title = metadata["title"]
  publication = metadata["publication"]
  published = metadata["published"]
  published = published.strftime("%Y-%m-%d")
  pdf_path = save_url_as_pdf(url, publication, title, published)

  event_template = f"""
from models import Event, Source

Event(
  date="",
  title="",
  description=\"\"\"
  
  \"\"\",
  people=[""],
  sources=[
    Source(
      title="{title}",
      publication="{publication}",
      published="{published}",
      url="{url}",
      article_copy="sources/{pdf_path}",
    ),
  ],
)
  """

  print(event_template)


if __name__ == "__main__":
  initialize_event(
    "https://www.politico.com/news/2020/03/25/trump-coronavirus-national-security-council-149285")

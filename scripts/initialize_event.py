import os
import re
import subprocess
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


def get_title(url):
  """
  Get the metadata title, for example:
  <meta data-rh="true" property="og:title" content="White House Blocks C.D.C. Guidance Over ..."/>
  """
  content = requests.get(url).content
  soup = BeautifulSoup(content, features="html.parser")
  title = soup.find("meta", attrs={"property": "og:title"}).get("content")
  return title


def initialize_event(url):
  """
  Create the Source for an Event at the given url
  """
  if url.startswith("https://www.nytimes.com"):
    publication = "The New York Times"
    match = re.search(r"https://www\.nytimes\.com/([0-9]{4})/([0-9]{2})/([0-9]{2})", url)
    if not match:
      print(f"Could not find date in url: {url}")
      return
    year, month, day = match.groups()

  elif url.startswith("https://www.washingtonpost.com"):
    publication = "The Washington Post"
    match = re.search(r"/([0-9]{4})/([0-9]{2})/([0-9]{2})/", url)
    if not match:
      print(f"Could not find date in url: {url}")
      return
    year, month, day = match.groups()

  else:
    print(f"Not sure how to parse publication: {url}")
    return

  published = f"{year}-{month}-{day}"
  title = get_title(url)
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
  initialize_event("https://www.nytimes.com/2020/05/11/us/politics/white-house-masks-trump-coronavirus.html")

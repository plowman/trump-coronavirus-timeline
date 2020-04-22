from models import Event, Source

NOVEL_CORONAVIRUS_CHINA = Source(title="Novel Coronavirus – China", publication="WHO", published="2020-01-12",
           url="https://www.who.int/csr/don/12-january-2020-novel-coronavirus-china/en/",
           article_copy="sources/2020-01-12-who-novel-coronavirus.pdf", )

Event(
  date="2020-01-12",
  title="WHO notifies the world of a 'novel coronavirus' and its first death",
  description="""
  This is the second serious warning the WHO sent out, and the first time the WHO was sure it was a new coronavirus.
  """,
  orgs=["WHO"],
  sources=[
    NOVEL_CORONAVIRUS_CHINA
  ],
)

Event(
  date="2020-01-12",
  title="China shares coronavirus genetic sequence",
  description="""
  Starting at this point, countries could start creating tests for the virus.
  """,
  sources=[
    NOVEL_CORONAVIRUS_CHINA,
  ],
)

from models import Event, Source

Event(
  date="2020-01-05",
  title="WHO notifies the world of a 'Pneumonia of Unknown Cause'",
  description="""
  This is the first warning the WHO sent about the novel coronavirus.
  """,
  orgs=["WHO"],
  sources=[
    Source(
      title="Pneumonia of unknown cause – China",
      publication="WHO",
      published="2020-01-05",
      url="https://www.who.int/csr/don/05-january-2020-pneumonia-of-unkown-cause-china/en/",
      article_copy="sources/2020-01-05-who-pneumonia-of-unknown-cause.pdf",
    ),
  ],
)

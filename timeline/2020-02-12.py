from models import Event, Source

Event(
  date="2020-02-12",
  title="CDC admits its testing kits are flawed",
  description="""
  One week after first shipping the tests to labs in the US and around the world, the CDC confirmed its test doesn't 
  work. Our ability to understand how the virus is spreading in the US is severely limited.
  """,
  orgs=["CDC"],
  sources=[
    Source(
      title="Coronavirus Test Kits Sent to States Are Flawed, C.D.C. Says",
      publication="The New York Times",
      published="2020-02-12",
      url="https://www.nytimes.com/2020/02/12/health/coronavirus-test-kits-cdc.html",
      article_copy="sources/2020-02-12-new-york-times-test-kits-are-flawed.pdf",
    ),
  ],
)

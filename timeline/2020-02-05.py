from models import Event, Source

Event(
  date="2020-02-05",
  title="CDC begins distributing flawed test kits to labs around the country",
  description="""
  Although we did not know it at the time, we would later learn that the CDC tests suffered from a technical flaw and 
  didn't produce reliable results.
  """,
  people=[],
  sources=[
    Source(
      title="Shipping of CDC 2019 Novel Coronavirus Diagnostic Test Kits Begins",
      publication="CDC",
      published="2020-02-06",
      url="https://www.cdc.gov/media/releases/2020/p0206-coronavirus-diagnostic-test-kits.html",
      article_copy="./sources/2020-02-06-cdc-shipping-tests.pdf",
    ),
  ],
)

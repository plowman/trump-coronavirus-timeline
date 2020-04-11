from models import Event, Source

Event(
  date="2020-02-29",
  title="WHO has shipped tests to 60 countries, and the US is not among them.",
  description="""
  Three weeks after releasing flawed CDC tests, the US has still not requested the WHO tests. The bottleneck is clearly
  not the WHO because at this point the WHO has sent tests to 60 countries.
  """,
  people=[],
  sources=[
    Source(
      title="How testing failures allowed coronavirus to sweep the U.S.",
      publication="Politico",
      published="2020-03-06",
      url="https://www.politico.com/news/2020/03/06/coronavirus-testing-failure-123166",
      article_copy="./sources/2020-03-06-politico-how-testing-failures.pdf",
    ),
  ],
)

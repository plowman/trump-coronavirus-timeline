from models import Event, Source

Event(
  date="2017-01-20",
  title="Obama gives Trump administration a pandemic handbook, which they will later ignore",
  description="""
  From the article,
  > The 69-page document, finished in 2016, provided a step by step list of priorities - which were then ignored 
  by the administration.
  """,
  sources=[
    Source(
      title="Trump team failed to follow NSC’s pandemic playbook",
      publication="Politico",
      published="2020-03-25",
      url="https://www.politico.com/news/2020/03/25/trump-coronavirus-national-security-council-149285",
      article_copy="sources/2020-03-21-politico-trump-team-failed-to-follow-nsc-pandemic-playbook.pdf",
    ),
  ],
)

from models import Event, Source

Event(
  date="2020-03-24",
  title="Trump says of providing aid to states 'it’s a two-way street. They have to treat us well also.'",
  description="""
  As usual, the full quote is extremely dense Trump gibberish, so it's hard to know exactly what he's saying. However,
  there is no other plausible interpretation of "They have to treat us well also" in this context except that it will be
  worse for states if they don't.
  
  The Trump quote is this:
  > No, I think we’re doing very well. But, you know, it’s a two-way street. They have to treat us well also. They can’t
  say, “Oh gee, we should get this, we should get that.” We’re doing a great job, like in New York, where we’re 
  building, as I said, four hospitals, four medic — we’re literally building hospitals and medical centers. And 
  then I hear that, you know, there’s a problem with ventilators.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump commits to helping blue states fight the coronavirus — if their governors are nice to him",
      publication="Vox",
      published="2020-03-25",
      url="https://www.vox.com/2020/3/25/21193803/trump-to-governors-coronavirus-help-ventilators-cuomo",
      article_copy="./sources/2020-03-25-vox-trump-governors-treat-us-well.pdf",
    ),
    Source(
      title="Did Trump Say Governors Had To Treat Him Well To Get COVID-19 Supplies?",
      publication="Snopes",
      published="2020-03-27",
      url="https://www.snopes.com/fact-check/trump-governors-supplies/",
      article_copy="./sources/2020-03-27-snopes-did-trump-say-governors-have-to-treat-him-well.pdf",
    ),
  ],
)

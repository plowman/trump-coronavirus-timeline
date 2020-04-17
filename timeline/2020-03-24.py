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

Event(
  date="2020-03-24",
  title="Trump wants country ‘opened up and raring to go’ by Easter",
  description="""
  His exact quote was,
  > I would love to have the country opened up and just er raring to go by Easter.
  
  As if trying to out-do himself, he added,
  > We lose thousands and thousands of people a year to the flu, but we don’t turn the country off. We lose much more 
  than that to automobile accidents. We don’t call the automobile companies and say, ‘Stop making automobiles.’
  
  Finally, he said,
  > We’re all working very hard to make that a reality. Easter is a very special day for a lot of reasons. What a great 
  timeline that would be.
  
  Unfortunately, no journalist asked him to enumerate any of the reasons that Easter is a "special day." 
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump wants U.S. economy ‘opened up and raring to go’ by Easter",
      publication="The Washington Post",
      published="2020-03-24",
      url="https://www.washingtonpost.com/health/trump-wants-us-economy-opened-up-and-raring-to-go-by-easter/2020/03/24/dced0a12-6d65-11ea-b148-e4ce3fbd85b5_story.html",
      article_copy="sources/2020-03-24-washington-post-trump-raring-to-go-by-easter.pdf",
    ),
  ],
)

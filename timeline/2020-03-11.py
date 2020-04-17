from models import Event, Source

Event(
  date="2020-03-11",
  title="World Health Organization declares covid-19 a pandemic",
  description="""
  The director of the WHO declared that they consider covid-19 to be a pandemic.
  """,
  people=[],
  sources=[
    Source(
      title="WHO Director-General's opening remarks at the media briefing on COVID-19 - 11 March 2020",
      publication="World Health Organization",
      published="2020-03-11",
      url="https://www.who.int/dg/speeches/detail/who-director-general-s-opening-remarks-at-the-media-briefing-on-covid-19---11-march-2020",
      article_copy="sources/2020-03-11-who-director-declares-pandemic.pdf",
    ),
  ],
)

Event(
  date="2020-03-11",
  title="Trump botches travel ban announcement, says he's banning all travel and cargo",
  description="""
  He terrified Americans traveling in Europe and tanked the markets by falsely stating that all goods and people would 
  be banned starting on March 13th at midnight.
  
  The first problematic quote was this:
  > To keep new cases from entering our shores, we will be suspending all travel from Europe to the United States for 
  the next 30 days.
  
  In reality, Americans were still allowed to return to the US. Claiming that "all travel" was being suspended caused
  Americans abroad to start panic buying expensive flights home because they were afraid they would get stuck in Europe.

  The second problematic quote was this:
  > "[...] these prohibitions will not only apply to the tremendous amount of trade and cargo but various other things 
  as we get approval. Anything coming from Europe to the United States is what we are discussing."
  
  In reality, the prohibitions did not apply to cargo.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Suspends All Travel From Europe For 30 Days To Combat COVID-19",
      publication="NPR",
      published="2020-03-11",
      url="https://www.npr.org/2020/03/11/814597993/trump-set-to-deliver-address-as-coronavirus-deemed-a-pandemic",
      article_copy="sources/2020-03-11-npr-trump-announces-european-travel-ban.pdf",
    ),
  ],
)

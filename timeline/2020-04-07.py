from models import Event, Source

Event(
  date="2020-04-07",
  title="Trump removes inspector general who would oversee $2 trillion stimulus spending",
  description="""
  Trump removed Glenn Fine, the chairman of the federal panel Congress created to oversee his administration’s 
  management of the $2 trillion coronavirus stimulus package.
  
  To explain his move, Trump said, “We have a lot of IGs in from the Obama era,” he said Tuesday. “And as you know, it’s
  a presidential decision. And I left them, largely. I mean, changed some, but I left them. . . . But when we have, you 
  know, reports of bias and when we have different things coming in. I don’t know Fine. I don’t think I ever met Fine.”
  """,
  people=["Trump", "Glenn Fine"],
  sources=[
    Source(
      title="Trump removes inspector general who was to oversee $2 trillion stimulus spending",
      publication="The Washington Post",
      published="2020-04-07",
      url="https://www.washingtonpost.com/national-security/trump-removes-inspector-general-who-was-to-oversee-2-"
          "trillion-stimulus-spending/2020/04/07/2f0c6cb8-78ea-11ea-9bee-c5bf9d2e3288_story.html",
      article_copy="./sources/2020-04-07-washington-post-trump-removes-inspector-general.pdf",
    ),
  ],
)

Event(
  date="2020-04-07",
  title="Trump threatens to stop funding the WHO",
  description="""
  "We’re going to put a hold on money spent to the W.H.O. We’re going to put a very powerful hold on it and we’re going 
  to see," Trump said during the daily coronavirus briefing at the White House. He added, "They called it wrong. They 
  call it wrong. They really, they missed the call."
  
  The claim that "they missed the call" is obviously a lie. The WHO declared a “public health emergency of international
  concern” weeks before Mr. Trump declared a national emergency.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Attacks W.H.O. Over Criticisms of U.S. Approach to Coronavirus",
      publication="The New York Times",
      published="2020-04-07",
      url="https://www.nytimes.com/2020/04/07/us/politics/coronavirus-trump-who.html",
      article_copy="./sources/2020-04-07-new-york-times-trump-attacks-who.pdf",
    ),
  ],
)

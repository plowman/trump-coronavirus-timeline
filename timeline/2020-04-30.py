from models import Event, Source

Event(
  date="2020-04-30",
  title="Trump pushes narrative that coronavirus originated in Wuhan labs",
  description="""
  He is instructing Secretary of State Mike Pompeo to push the intelligence agencies to find a link between a Wuhan lab 
  and the coronavirus. Until he gets the evidence he needs, he's just saying it might be true and hoping the facts catch
  up.
  
  Trump's quote is:
  > “It’s a terrible thing that happened, whether they made a mistake or whether it started off as a mistake and then 
  they made another one, or did somebody do something on purpose? [...] There are a lot of theories, but we have people 
  looking at it very, very strongly. Scientific people, intelligence people, and others.”
  
  From the article:
  > Senior Trump administration officials have pushed American spy agencies to hunt for evidence to support an 
  unsubstantiated theory that a government laboratory in Wuhan, China, was the origin of the coronavirus outbreak, 
  according to current and former American officials.
  
  Why it matters: Having messed up the response, Trump is now searching as hard as he can for a scapegoat. Blaming China
  for literally manufacturing the virus is too juicy for Trump to resist.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Officials Are Said to Press Spies to Link Virus and Wuhan Labs",
      publication="The New York Times",
      published="2020-04-30",
      url="https://www.nytimes.com/2020/04/30/us/politics/trump-administration-intelligence-coronavirus-china.html",
      article_copy="sources/2020-04-30-new-york-times-trump-pushing-lab-conspiracy-theory.pdf",
    ),
  ],
)

from models import Event, Source

Event(
  date="2020-05-01",
  title="Trump replacing HHS watchdog because she identified critical medical shortages",
  description="""
  Trump nominated a replacement for Health and Human Services inspector general Christi Grimm. Grimm published a report 
  on April 3rd where she surveyed 323 hospitals and asked what their biggest challenges were responding to the pandemic.
  Among the hospitals' concerns were severe shortages of testing supplies and long waits for results.
  
  Trump found out about the report on April 6th, when he had this exchange with a reporter:
  > Reporter: Despite the nearly 1.8 million tests that you say the United States has done, the Inspector General for 
  the Department of Health and Human Services released a report today — a survey — of more than 300 hospitals across the 
  country.  And the number one complaint from those hospitals were severe shortages of testing supplies and a really 
  long wait time.
  
  > THE PRESIDENT:  It’s just wrong.  Did I hear the word “inspector general”?  Really?  It’s wrong.  And they’ll talk 
  to you about it.  It’s wrong.
  
  > Reporter: But this is your own government.
  
  > THE PRESIDENT:  Uh, it’s — well, where did he come from — the inspector general?  What’s his name?
  
  Why it matters: Trump doesn't care about fixing the problems. He only cares about silencing the criticism.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Moves to Replace Watchdog Who Identified Critical Medical Shortages",
      publication="The New York Times",
      published="2020-05-01",
      url="https://www.nytimes.com/2020/05/01/us/politics/trump-health-department-watchdog.html",
      article_copy="sources/2020-05-01-trump-fires-hhs-ig.pdf",
    ),
  ],
)

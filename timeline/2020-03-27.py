from models import Event, Source

Event(
  date="2020-03-27",
  title="Trump says if governors \"don’t treat you right, I don’t call.\"",
  description="""
  He said "If they don’t treat you right, I don’t call."
  
  Here is the full exchange:
  > [Pence] calls all the governors.  I tell him — I mean, I’m a different type of person — I say, “Mike, don’t call the 
  governor of Washington.  You’re wasting your time with him.  Don’t call the woman in Michigan.”  All — it doesn’t make
  any difference what happens —

  > Q You don’t want him to call the governor of Washington?

  > THE PRESIDENT:  No, no.  You know what I say?  If they don’t treat you right, I don’t call.  He’s a different type 
  of person.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump to Governors: I’d Like You to Do Us a Favor, Though",
      publication="The New York Times",
      published="2020-03-30",
      url="https://www.nytimes.com/2020/03/30/opinion/trump-federal-aid-coronavirus.html",
      article_copy="sources/2020-03-30-new-york-times-trump-federal-aid-coronavirus.pdf",
    ),
    Source(
      title="Remarks by President Trump, Vice President Pence, and Members of the Coronavirus Task Force in Press Briefing",
      publication="WhiteHouse.gov",
      published="2020-03-27",
      url="https://www.whitehouse.gov/briefings-statements/remarks-president-trump-vice-president-pence-members-coronavirus-task-force-press-briefing-13/",
      article_copy="sources/2020-03-27-white-house-trump-press-briefing.pdf",
    ),
  ],
)

from models import Event, Source

Event(
  date="2020-02-06",
  title="First death in the US from coronavirus, unknown in cause until later",
  description="""
  Although we didn't know it at the time, on Feb 6th, the first person died in the US of coronavirus. The person died in
  their home. It wasn't until April that we confirmed coronavirus was to blame.

  From the article,
  > The county’s medical examiner-coroner said that autopsies of two people who died at their homes on Feb. 6 and 
  Feb. 17 showed that the individuals were infected with the virus.
  
  Why it matters: if we had spun up testing sooner or started doing better tracking of Americans returning from China,
  we could have known this was happening so much sooner.
  """,
  sources=[
    Source(
      title="Coronavirus Death in California Came Weeks Before First Known U.S. Death",
      publication="The New York Times",
      published="2020-04-22",
      url="https://www.nytimes.com/2020/04/22/us/coronavirus-first-united-states-death.html",
      article_copy="sources/2020-04-22-new-york-times-first-death-in-the-us.pdf",
    ),
  ],
)

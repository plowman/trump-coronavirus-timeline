from models import Event, Source

Event(
  date="2020-04-21",
  title="Trump announces ban on green cards, backs down from broader immigration ban",
  description="""
  Trump said he would suspend issuing new green cards for 60 days. Earlier he had threatened a more complete immigration
  ban.
  
  His quote on this is:
  > “By pausing immigration, we will help put unemployed Americans first in line for jobs as America reopens. So 
  important, It would be wrong and unjust for Americans laid off by the virus to be replaced with new immigrant labor 
  flown in from abroad. We must first take care of the American worker.”
  
  Why it matters: immigration has nothing to do with the coronavirus. And slowing down immigration won't help the 
  economy recover any faster. Trump is still fishing for things he can do to make him seem like the economic failures 
  are not his fault. Shifting blame to immigrants has always been part of his playbook.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Halts New Green Cards, but Backs Off Broader Immigration Ban",
      publication="The New York Times",
      published="2020-04-21",
      url="https://www.nytimes.com/2020/04/21/us/politics/coronavirus-trump-immigration-ban.html",
      article_copy="sources/2020-04-21-new-york-times-immigration-ban.pdf",
    ),
  ],
)

Event(
  date="2020-04-21",
  title="368 patient study shows patients taking Hydroxychloroquine dying at higher rates",
  description="""
  In fact, the death rate was higher in patients treated with Hydroxychloroquine (HC) even though the rate of 
  ventilation was the same. This is a pretty big hint that even among patients who have a very serious case of covid,
  taking HC makes things worse.

  Why it matters: after weeks of pushing HC without any evidence, Trump will now never mention it again. But it's 
  important that we remember this: if he hadn't pushed it so hard then fewer people would have died.
  """,
  sources=[
    Source(
      title="New U.S. Treatment Guidelines for Covid-19 Don’t See Much Progress",
      publication="New York Times",
      published="2020-04-21",
      url="https://www.nytimes.com/2020/04/21/health/nih-covid-19-treatment.html",
      article_copy="sources/2020-04-21-new-york-times-nih-covid19-treatment.pdf",
    ),
    Source(
      title="Outcomes of hydroxychloroquine usage in United States veterans hospitalized with Covid-19",
      publication="MedRxiv",
      published="2020-04-21",
      url="https://www.medrxiv.org/content/10.1101/2020.04.16.20065920v1",
      article_copy="sources/2020-04-21-medrxiv-hydroxychloroquine-study-results.pdf",
    ),
  ],
)

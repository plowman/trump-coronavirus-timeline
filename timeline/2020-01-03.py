from models import Event
from timeline.shared_sources import THE_LOST_MONTH

Event(
  date="2020-01-03",
  title="CDC director notifies HHS secretary of how terrified China CDC director is",
  description="""
  CDC director Redfield received a call from the where the China CDC director burst out crying because of how bad things
  were getting in Wuhan. Shortly after, he notified the HHS Secretary, Alex Azar, about the serverity of the outbreak.
  """,
  people=["Redfield", "Azar"],
  orgs=["HHS", "CDC"],
  sources=[
    THE_LOST_MONTH,
  ],
)

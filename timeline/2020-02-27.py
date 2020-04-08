from models import Event
from timeline.shared_sources import COMPLETE_LIST_OF_TRUMP_DOWNPLAYING_CORONAVIRUS

Event(
  date="2020-02-27",
  title="Trump says coronavirus will disappear: 'One day, it’s like a miracle, it will disappear.'",
  description="""
  Trump said: "It's going to disappear. One day -- it's like a miracle -- it will disappear. And from our shores, we 
  -- you know, it could get worse before it gets better. It could maybe go away. We'll see what happens. Nobody really 
  knows. The fact is, the greatest experts -- I've spoken to them all. Nobody really knows."
  """,
  people=["Trump"],
  sources=[
    COMPLETE_LIST_OF_TRUMP_DOWNPLAYING_CORONAVIRUS,
  ],
)

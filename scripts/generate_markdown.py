import os
import importlib

from models import ALL_EVENTS


def import_all_events():
  scripts_folder = os.path.dirname(__file__)
  project_folder = os.path.dirname(scripts_folder)
  timeline_folder = os.path.join(project_folder, 'timeline')

  for file in os.listdir(timeline_folder):
    if file.startswith('20') and file.endswith('.py'):
      file = file.replace('.py', '')
      importlib.import_module(f'timeline.{file}')


def format_date(date):
  return date.strftime("%b %-d, %Y")


def generate_markdown():
  import_all_events()

  timeline_markdown = "# Trump Covid Timeline\n\n"
  previous_date = None
  for event in sorted(ALL_EVENTS, key=lambda x: x.date):
    if event.date != previous_date:
      timeline_markdown += f"### {format_date(event.date)}"
      previous_date = event.date

    source = event.sources[0]
    event.description = event.description.strip()
    timeline_markdown += f"""
#### {event.title}
{event.description}

Source: [{source.publication}]({source.url}) on {format_date(source.published)}.
"""

  scripts_folder = os.path.dirname(__file__)
  project_folder = os.path.dirname(scripts_folder)
  timeline_path = os.path.join(project_folder, 'timeline.md')
  with open(timeline_path, mode='w+') as timeline_file:
    timeline_file.write(timeline_markdown)


generate_markdown()

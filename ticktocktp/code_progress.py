from rich.progress import Progress, BarColumn, TextColumn, ProgressColumn
import time

class SecondsRemainingColumn(ProgressColumn):
	def render(self, task):
		return f"{int(task.completed)}s"

def show_countdown(description, seconds=30):
	with Progress(
		TextColumn("[progress.description]{task.description}"),
		BarColumn(),
		SecondsRemainingColumn(),
	) as progress:
		task = progress.add_task(description, total=seconds)
		for remaining in range(seconds, -1, -1):
			progress.update(task, completed=remaining)
			time.sleep(1)
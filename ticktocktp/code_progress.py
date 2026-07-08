from rich.progress import Progress, BarColumn, TextColumn, ProgressColumn
import time

class SecondsRemainingColumn(ProgressColumn):
	def render(self, task):
		return f"{int(task.completed)}s"

def show_countdown(description, progress=0, seconds=30):
	with Progress(
		TextColumn("[progress.description]{task.description}"),
		BarColumn(),
		SecondsRemainingColumn(),
	) as progress_bar:
		task = progress_bar.add_task(description, total=seconds)
		start = seconds - progress
		for remaining in range(start, -1, -1):
			progress_bar.update(task, completed=remaining)
			time.sleep(1)
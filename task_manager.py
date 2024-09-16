from datetime import datetime, timedelta


class Task:

	def __init__(self, title, description):
		self.title = title
		self.description = description
		self.completed = False
		self.created_at = datetime.now().isoformat()


class Task_Two:

	def __init__(self, title, description, completed, created_at):
		self.title = title
		self.description = description
		self.completed = completed
		self.created_at = created_at

class TaskManager:

	def __init__(self, storage):
		self.storage = storage

	def add_task(self, title, description):
		task = Task(title, description)
		self.storage.save_task(task)
		return task

	def complete_task(self, title):
		task = self.storage.get_task(title)
		if task:
			task.completed = True
			self.storage.update_task(task)
			return True
		return False

	def list_tasks(self, include_completed=False):
		tasks = self.storage.get_all_tasks(include_completed)
		return tasks
	def calculate_avg_duration(self, tasks, completed_tasks):
		total_duration = timedelta()
		for task in tasks:
			total_duration = datetime.fromisoformat(task.created_at)
			total_duration = total_duration.hour
			hours = total_duration + total_duration
			if completed_tasks > 0:
				hours = hours / completed_tasks
			return hours

	def generate_report(self):
		tasks = self.storage.get_all_tasks(include_completed=True)
		total_tasks = len(tasks)
		completed_tasks = len([task for task in tasks if task.completed])
		avg_time = self.calculate_avg_duration(tasks,completed_tasks)
		report = {
		    "total": total_tasks,
		    "completed": completed_tasks,
		    "pending": total_tasks - completed_tasks,
			"avg_time": avg_time
		}
		
		return report


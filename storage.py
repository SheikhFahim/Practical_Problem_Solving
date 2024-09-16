import os
from task_manager import Task_Two
class Storage:

	def __init__(self):
		self.clear_all_tasks()
		# Check if the file exists
		self.read_tasks()

	def save_task(self, task):
		self.tasks.append(task)
		self.write_tasks()

	def update_task(self, updated_task):
		for i, task in enumerate(self.tasks):
			if task.title == updated_task.title:
				self.tasks[i] = updated_task
				break
		self.write_tasks()

	def get_task(self, title):
		for task in self.tasks:
			if task.title == title:
				return task
		return None

	def get_all_tasks(self,include_completed=False):
		self.clear_all_tasks()
		self.read_selective_list(include_completed)
		return list(self.tasks)

	def clear_all_tasks(self):
		self.tasks = []

	def read_tasks(self,include_completed=False):
		if os.path.exists('tasks.txt') and os.path.getsize('tasks.txt') > 0:
    	# Do something if the file exists
			with open('tasks.txt', 'r') as file:
				for line in file:
					title, description, completed, created_at = line.strip().split(',')
					self.completed = completed == 'True'
					task = Task_Two(title, description, self.completed, created_at)
					self.tasks.append(task)
		else:
    	# Ignore if the file does not exist
			pass
	def write_tasks(self):
		with open('tasks.txt', 'w') as file:
			for tasks in self.tasks:
				file.write(f"{tasks.title},{tasks.description},{tasks.completed},{tasks.created_at}\n")

	def read_selective_list(self,include_completed=False):
		if os.path.exists('tasks.txt') and os.path.getsize('tasks.txt') > 0:
    	# Do something if the file exists
			with open('tasks.txt', 'r') as file:
				for line in file:
					title, description, completed, created_at = line.strip().split(',')
					self.completed = completed == 'True'
					task = Task_Two(title, description, self.completed, created_at)
					if (include_completed == False):
						if(self.completed == False):
							self.tasks.append(task)
					else:
						self.tasks.append(task)
		else:
    	# Ignore if the file does not exist
			pass
import datetime

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, deadline):
        self.tasks.append({'task': task, 'deadline': deadline})

    def show_tasks_for_day(self, date):
        tasks_for_day = [task for task in self.tasks if task['deadline'].date() == date.date()]
        
        if not tasks_for_day:
            print("No tasks for the day.")
        else:
            print(f"Tasks for {date.date()}:")
            for task in tasks_for_day:
                print(f"- {task['task']} (Deadline: {task['deadline'].strftime('%Y-%m-%d %H:%M:%S')})")

if __name__ == "__main__":
    task_scheduler = TaskScheduler()

    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. Show Tasks for Today")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            task = input("Enter task description: ")
            deadline_str = input("Enter task deadline (YYYY-MM-DD HH:MM:SS): ")
            deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d %H:%M:%S')
            task_scheduler.add_task(task, deadline)
            print("Task added successfully!")

        elif choice == '2':
            today = datetime.datetime.now()
            task_scheduler.show_tasks_for_day(today)

        elif choice == '3':
            print("Exiting Task Scheduler. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

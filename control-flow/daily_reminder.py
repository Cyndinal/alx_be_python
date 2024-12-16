from babel.messages.checkers import checkers

task = input("Task description: ")
priority = input("Task priority: low/medium/high ").lower()
time_bound = input("Task time bound: yes/no ").lower()

task_template = {
    "task": task,
    "priority":priority,
    "time_bound":time_bound
}

match priority:
    case "high":
        if priority == "high" and time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")

    case "low":
        if priority == "low" and time_bound == "yes":
            print(f"{task_template.get(task)} is a low priority task. Consider completing it when you have free time")
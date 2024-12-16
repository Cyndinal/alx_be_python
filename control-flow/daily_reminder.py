from babel.messages.checkers import checkers

Task = input("Task description: ")
Priority = input("Task priority: low/medium/high ").lower()
Time_bound = input("Task time bound: yes/no ").lower()

task_template = {
    "task": Task,
    "priority":Priority,
    "time_bound":Time_bound
}

match Priority:
    case "high":
        if Priority == "high" and Time_bound == "yes":
            print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")

    case "low":
        if Priority == "low" and Time_bound == "yes":
            print(f"{task_template.get(Task)} is a low priority task. Consider completing it when you have free time")


"""
put\s*\(\s*['\"]Enter your task:\s*['\"]\s*\) / /
tmp/correction/2725873861510670660907599552428446824838_5/100740/988866/control-flow
/daily_reminder.py doesn't contain input\s*\(\s*['\"]Is it time-bound\?\s*\(yes\/no\):\s*['\"]\s*\) /
/tmp/correction/2725873861510670660907599552428446824838_5/100740/988866/control-flow/daily_reminder.py doesn't
contain input\s*\(\s*['\"]Priority\s*\(high\/medium\/low\):\s*['\"]\s*\)

"""

Task = input("Enter your task: ")
Priority = input("Priority:high/medium/low ").lower()
Time_Bound = input("Is it time-bound?(yes or no) ").lower()

task_template = {
    "task": Task,
    "priority":Priority,
    "time_bound":Time_Bound
}

match Priority:
    case "high":
        if Priority == "high" and Time_Bound == "yes":
            print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")

    case "low":
        if Priority == "low" and Time_Bound == "yes":
            print(f"{task_template.get(Task)} is a low priority task. Consider completing it when you have free time")
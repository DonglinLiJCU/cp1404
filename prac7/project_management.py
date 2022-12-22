"""
Project Management
Estimate: 20 minutes
Actual:    minutes
"""

from prac7.project import Project
import datetime


def main():
    projects = load_projects()
    show_menu()
    choices = ['L', 'S', 'D', 'F', 'A', 'U', 'Q']
    choice = input(">>> ")
    while choice.upper() != 'Q':
        if choice.upper() not in choices:
            print("Invalid choice, enter again:")
        else:
            if choice.upper() == 'D':
                projects_tuple = display_projects(projects)
                print("Incomplete projects:")
                for incomplete_project in projects_tuple[0]:
                    print(incomplete_project)
                print("Completed projects:")
                for completed_project in projects_tuple[1]:
                    print(completed_project)
                print()
        show_menu()
        choice = input(">>> ")
    print("Thank you for using custom-built project management software.")


def show_menu():
    menu = ["- (L)oad projects",
            "- (S)ave projects",
            "- (D)isplay projects",
            "- (F)ilter projects by date",
            "- (A)dd new project",
            "- (U)pdate project",
            "- (Q)uit"]
    for item in menu:
        print(item)


def load_projects(name="projects.txt"):
    projects = []
    in_file = open(name, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        name = parts[0]
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)
    return projects


def display_projects(projects):
    incomplete = []
    completed = []
    for project in projects:
        if project.is_completed() is True:
            completed.append(project)
        else:
            incomplete.append(project)
    completed.sort()
    incomplete.sort()
    return incomplete, completed


main()

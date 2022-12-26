"""
Project Management
Estimate: 40 minutes
Actual:   45 minutes
"""

from prac7.project import Project
import datetime


def main():
    file_name = "projects.txt"
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

            elif choice.upper() == 'L':
                last_name = file_name
                try:
                    file_name = input("Enter file name: ")
                    projects = load_projects(file_name)
                except FileNotFoundError:
                    print("File not found.")
                    file_name = last_name
                except:
                    print("Error loading file.")
                    file_name = last_name
                print()

            elif choice.upper() == 'S':
                out_file_name = input("Enter file name: ")
                save_projects(projects, out_file_name)

            elif choice.upper() == 'F':
                try:
                    start_date = input("Enter start date (dd/mm/yyyy): ")
                    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                    tmp_projects = filter_projects(projects, start_date)
                    for project in tmp_projects:
                        print(project)
                except ValueError:
                    print("Invalid date.")

            elif choice.upper() == 'A':
                print("Let's add a new project")
                try:
                    name = input("Name: ")
                    start_date = input("Start date (dd/mm/yyyy): ")
                    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                    priority = int(input("Priority: "))
                    cost_estimate = float(input("Cost estimate: $"))
                    completion_percentage = int(input("Percent complete: "))
                    while not 0 <= completion_percentage <= 100:
                        print("Invalid percentage")
                        completion_percentage = int(input("Percent complete: "))
                    projects = add_project(projects, name, start_date, priority, cost_estimate, completion_percentage)
                except ValueError:
                    print("Invalid input.")

            elif choice.upper() == 'U':
                for i in range(len(projects)):
                    print(f"{i} {projects[i]}")
                choice = int(input("Project choice: "))
                while not 0 <= choice <= len(projects) - 1:
                    print("Invalid choice")
                    choice = int(input("Project choice: "))
                print(projects[choice])
                new_percentage = input("New percentage: ")
                if new_percentage != '':
                    try:
                        new_percentage = int(new_percentage)
                        while not 0 <= new_percentage <= 100:
                            print("Invalid percentage")
                            new_percentage = int(input("New percentage: "))
                    except ValueError:
                        print("Invalid input.")
                else:
                    new_percentage = projects[choice].completion_percentage
                new_priority = input("New priority: ")
                if new_priority != '':
                    try:
                        new_priority = int(new_priority)
                        while new_priority < 0:
                            print("Invalid priority")
                            new_percentage = int(input("New priority: "))
                    except ValueError:
                        print("Invalid input.")
                else:
                    new_priority = projects[choice].priority
                projects = update_project(projects,choice, new_percentage, new_priority)

        show_menu()
        choice = input(">>> ")
    save_projects(projects)
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


def save_projects(projects, out_file_name="projects.txt"):
    out_file = open(out_file_name, "w")
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        out_file.write(project.file_str() + "\n")
    out_file.close()


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


def filter_projects(projects, start_date: datetime):
    tmp_projects = []
    for project in projects:
        if project.start_date >= start_date:
            tmp_project = Project(project.name, project.start_date, project.priority, project.cost_estimate,
                                  project.completion_percentage)
            tmp_project.set_compare_mode(1)
            tmp_projects.append(tmp_project)
    tmp_projects.sort()
    return tmp_projects


def add_project(projects, name, start_date, priority, cost_estimate, completion_percentage):
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    return projects


def update_project(projects, choice, new_percentage, new_priority):
    projects[choice].update_completion(new_percentage)
    projects[choice].update_priority(new_priority)
    return projects


main()

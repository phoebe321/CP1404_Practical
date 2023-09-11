
import datetime
from prac_07.project import ProjectManagement


def main():
    MENU = "(L)oad projects\n" \
           "(S)ave projects\n" \
           "(D)isplay project\n" \
           "(F)ilter projects by date\n" \
           "(A)dd new projects\n" \
           "(U)pdate project\n" \
           "(Q)uit"

    projects = get_file('project.txt')
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            if filename != '':
                try:
                    projects = get_file(filename)
                    print(projects)
                except FileNotFoundError:
                    print('Invalid Filename')
        elif choice == "S":
            filename = input("Enter filename to be save:")
            save_file(projects, filename)
        elif choice == "D":
            complete_project, incomplete_project = check_project(projects)
            print("Incomplete projects: ")
            print("")
            print('Completed projects: ')
            display_projects(complete_project)
        elif choice == "F":
            is_valid = False
            while not is_valid:
                try:
                    date = input("Show projects that start after date (dd/mm/yyyy): ")
                    filtered_projects = filtered_date_projects(date, projects)  # Fixed function name
                    projects = sort_projects(filtered_projects)
                    display_projects(projects)
                    is_valid = True
                except ValueError:
                    print("Incorrect date format, should be dd/mm/yyyy")
                    date = input("Show projects that start after date (dd/mm/yyyy): ")
        elif choice == "A":
            print("lets add new project")
            try:
                name = input("Name: ")
                start_date = input("Start date (dd/mm/yyyy): ")
                priority = int(input("Priority: "))
                cost = input("Cost estimate: ")
                cost = int(cost)
                completion = input("Percent complete: ")
                project = ProjectManagement(str(name), str(start_date), int(priority),int(cost), int(completion))
                projects.append(project)
            except ValueError:
                print("Invalid input")

        elif choice == "U":
            project_choice = int(input("Project choice: "))  # Ask the user to choose a project
            if 0 <= project_choice < len(projects):
                project = projects[project_choice]  # Get the chosen project

                new_percentage = input("New Percentage: ")
                if new_percentage:
                    try:
                        new_percentage = int(new_percentage)
                        project.update_percentage(new_percentage)  # Update completion percentage
                    except ValueError:
                        print("Invalid input. Please enter a valid integer for percentage.")

                new_priority = input("New Priority: ")
                if new_priority:
                    try:
                        new_priority = int(new_priority)
                        project.update_priority(new_priority)  # Update priority
                    except ValueError:
                        print("Invalid input. Please enter a valid integer for priority.")
            else:
                print("Invalid project choice. Please choose a valid project index.")
        else:
            print("Invalid choice!")
        choice = input(">>> ").upper()


def get_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read the file and return a list of ProjectManagement objects
            projects = []
            for line in file:
                parts = line.strip().split('\t')  # Assuming tab-separated data
                if len(parts) == 5:  # Ensure all fields are present
                    name, start_date, priority, cost, completion = parts
                    project = ProjectManagement(name, start_date, int(priority), int(cost), int(completion))
                    projects.append(project)
            return projects
    except FileNotFoundError:
        print('Invalid Filename')
        return []


def save_file(projects, filename):
    with open(filename, 'w') as file:
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion}\n")


def check_project(projects):
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    return complete_projects, incomplete_projects


def display_projects(projects):
    for project in projects:
        print(f"{project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost:.2f}, completion: {project.completion}%")


def filtered_date_projects(date, projects):
    try:
        date_obj = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date_obj > date_obj]
        return filtered_projects
    except ValueError:
        print("Incorrect date format, should be dd/mm/yyyy")
        return []


def sort_projects(projects):
    return sorted(projects, key=lambda x: x.priority)


if __name__ == '__main__':
    main()

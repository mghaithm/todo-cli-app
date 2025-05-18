import json
from colorama import Fore, Style, init
init(autoreset=True)


FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME,"r") as file: 
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks,file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["done"] else "[ ]"
        print(f"{index}. {Fore.GREEN + status if task['done'] else Fore.YELLOW + status} {Style.BRIGHT + task['title']}")

def add_task(tasks):
        title= input("Enter a task: ")
        tasks.append({"title": title, "done" : False})
        print(Fore.GREEN + "✅ Task added.")

def mark_done(tasks):
    show_tasks(tasks)
    number = int(input("Enter task number to mark as done: "))
    if 1<= number <= len(tasks):
        tasks[number - 1]["done"] = True
        print(Fore.YELLOW + "✔️ Task marked as done.")
    else:
        print(Fore.RED + "❌ Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print(Fore.CYAN + "\n=== TO-DO LIST MENU ===")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print(Fore.MAGENTA + "👋 Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

# Run the program
if __name__ == "__main__":
    main()
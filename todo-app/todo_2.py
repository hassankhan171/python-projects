# Length of Todo

# 1. Create Todo
# 2. View Todo
# 3. Update Todo
# 4. Delete Todo

class TodoList:
    tasks = []

    @staticmethod
    def welcome():
        print('Welcome to Contact Book')

    def menu(self):
        print('1. Create Task')
        print('2. View Task')
        print('3. Update Task')
        print('4. Delete Task')
        print('5. Search Task')  # --> optional
        print('6. Exit')
        choice = int(input('Choose: '))
        return choice

    def create_todo(self):
        try:
            length = int(input("Enter number of tasks: "))
            for i in range(1, length+1):
                task = input(f"Enter Task {i}: ").lower()
                self.tasks.append(task)

            print("Tasks append successfully")
        except Exception as e:
            print('Something went wrong')
            print('Error reason: ', e)

    def view_todos(self):
        try:
            if len(self.tasks) == 0:
                print('No record found')
            else:
                index = 1
                for item in self.tasks:
                    print(f"{index}: {item}")
                    index += 1
        except Exception as e:
            print('Something went wrong')
            print('Error reason: ', e)


    def update_todo(self):
        try:
            name = input("Enter the name of the task you want to update: ").lower()
            for i in range(len(self.tasks)):
                if self.tasks[i] == name:
                    new_task = input("Enter the new task: ").lower()
                    self.tasks[i] = new_task
                    print("Task updated successfully.")
                    return
            print(f"Task '{name}' does not exist.")

        except Exception as e:
            print('Something went wrong')
            print('Error reason:', e)

    def delete_todo(self):
        try:
            name = input("Enter the name of the task you want to delete: ").lower()
            for i in range(len(self.tasks)):
                if self.tasks[i] == name:
                    del self.tasks[i]
                    print("Task deleted successfully.")
                    return
            print(f"Task '{name}' does not exist.")
        except Exception as e:
            print('Something went wrong')
            print('Error reason:', e)


todo = TodoList()
TodoList.welcome()
while True:
    result = todo.menu()
    if result == 1:
        todo.create_todo()
    elif result == 2:
        todo.view_todos()
    elif result == 3:
        todo.update_todo()
    elif result == 4:
        todo.delete_todo()
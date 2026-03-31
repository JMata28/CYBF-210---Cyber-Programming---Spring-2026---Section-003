class Task:
    def __init__(self, description, next_task=None):
        self.description = description
        self.next_task = next_task

class ToDoList:
    def __init__(self, head_task):
        self.head_task = head_task

    def addTask(self, new_task):
        curr = self.head_task
        while(curr):
            if curr.next_task == None:
                break
            curr = curr.next_task
        curr.next_task = new_task
        return self.head_task
    
    def showTasks(self):
        curr = self.head_task
        list_of_tasks = []
        while(curr):
            list_of_tasks.append(str(curr.description))
            curr = curr.next_task
        print(' -> '.join(list_of_tasks))
    
    def deleteTask(self, description):
        curr = self.head_task

        # Edge case: list is empty
        if curr is None:
            print("The list is empty!")
            return None

        # Edge case: deleting the head node
        if curr.description == description:
            self.head_task = curr.next_task
            print(f"{description} Task was removed from the list!")
            return self.head_task
        
        # Traverse the list
        while curr.next_task:
            if curr.next_task.description == description:
                curr.next_task = curr.next_task.next_task
                print(f"{description} Task was removed from the list!")
                return self.head_task
            curr = curr.next_task

        print(f"{description} Task is not on the list so it can't be removed!")
        return self.head_task


A = Task("Buy cheese.")
B = Task("Buy sauce.")
C = Task("Buy crust.")
D = Task("Bake together.")

pizza_recipe = ToDoList(A)
pizza_recipe.head_task = pizza_recipe.addTask(B)
pizza_recipe.head_task = pizza_recipe.addTask(C)
pizza_recipe.head_task = pizza_recipe.addTask(D)
pizza_recipe.showTasks()

pizza_recipe.deleteTask("Buy crust.")
pizza_recipe.showTasks()

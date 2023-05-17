import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
user_prompt = "Type 'add', 'show', 'edit', 'complete', or 'exit': \n"

while True:
    command = input(user_prompt)
    command = command.strip()

    if command.startswith('add'):
        todo = command[4:]
        
        todo_list = functions.get_todos()
            
        todo_list.append(todo + '\n')
        
        functions.write_todos(todo_list)
        
    elif command.startswith('show'):
        todo_list = functions.get_todos()

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f'{index + 1}. {item}')
                 
    elif command.startswith('edit'):
        try:
            num = int(command[5:])
            num = num - 1
            
            todo_list = functions.get_todos()
            
            new_todo = input("Enter new todo: \n")
            todo_list[num] = new_todo + '\n'
            
            functions.write_todos(todo_list)
            
        except ValueError:
            print("Your command is not valid.")
            continue
            
    elif 'complete' in command:
        try:
            done = int(command[9:])
            
            todo_list = functions.get_todos('todo.txt')
                
            temp = todo_list[done-1].strip('\n')
            todo_list.pop(done-1)
            
            functions.write_todos(todo_list)
                
            print(f'To do - {temp} - has been marked as complete! \n')
        except IndexError:
            print("Out of range index.")
            continue
        
    elif command.startswith('exit'):
        break
    
    else:
        print("Unknown command")

print('Bye')
import requests
import json

# Base URL for the API
BASE_URL = "http://127.0.0.1:8000"

def test_create_todo():
    """Test creating a todo"""
    url = f"{BASE_URL}/todos"
    data = {
        "title": "Test Todo for Deletion",
        "description": "This is a test todo that will be deleted",
        "completed": False
    }
    
    response = requests.post(url, json=data)
    print(f"Create Todo Response: {response.status_code}")
    if response.status_code == 200:
        todo = response.json()
        print(f"Created Todo: {json.dumps(todo, indent=2)}")
        return todo["id"]
    else:
        print(f"Error creating todo: {response.text}")
        return None

def test_delete_todo(todo_id):
    """Test deleting a todo"""
    url = f"{BASE_URL}/todos/{todo_id}"
    
    response = requests.delete(url)
    print(f"Delete Todo Response: {response.status_code}")
    if response.status_code == 200:
        deleted_todo = response.json()
        print(f"Deleted Todo: {json.dumps(deleted_todo, indent=2)}")
        return True
    else:
        print(f"Error deleting todo: {response.text}")
        return False

def test_get_todos():
    """Test getting all todos"""
    url = f"{BASE_URL}/todos"
    
    response = requests.get(url)
    print(f"Get Todos Response: {response.status_code}")
    if response.status_code == 200:
        todos = response.json()
        print(f"Number of Todos: {len(todos)}")
        return todos
    else:
        print(f"Error getting todos: {response.text}")
        return []

def main():
    print("Testing delete functionality...")
    
    # Get initial todos
    print("\n1. Getting initial todos:")
    initial_todos = test_get_todos()
    
    # Create a test todo
    print("\n2. Creating a test todo:")
    todo_id = test_create_todo()
    
    if todo_id is not None:
        # Get todos after creation
        print("\n3. Getting todos after creation:")
        todos_after_creation = test_get_todos()
        
        # Delete the todo
        print(f"\n4. Deleting todo with ID {todo_id}:")
        success = test_delete_todo(todo_id)
        
        if success:
            # Get todos after deletion
            print("\n5. Getting todos after deletion:")
            todos_after_deletion = test_get_todos()
            
            print(f"\nSummary:")
            print(f"- Initial todos: {len(initial_todos)}")
            print(f"- After creation: {len(todos_after_creation)}")
            print(f"- After deletion: {len(todos_after_deletion)}")
            
            if len(initial_todos) == len(todos_after_deletion):
                print("[SUCCESS] Delete functionality is working correctly!")
            else:
                print("[ERROR] Delete functionality may have issues.")
        else:
            print("[ERROR] Failed to delete the todo.")
    else:
        print("[ERROR] Failed to create a test todo.")

if __name__ == "__main__":
    main()
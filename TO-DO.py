import mysql.connector as mysql

# Database Connection
def connect_db():
    return mysql.connect(host="localhost", user="root", passwd="MySQL Password", database="TODO")

# Initialize Database & Table
def setup_database():
    conn = mysql.connect(host="localhost", user="root", passwd="MySQL Password")
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS TODO")
    cursor.execute("USE TODO")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_todo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task VARCHAR(50) NOT NULL,
            status ENUM('pending', 'completed') DEFAULT 'pending'
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database & Table ready.")

# Insert Task
def insert_task():
    task = input("Enter task: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Task added successfully!")

# View All Tasks
def view_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tb_todo")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if tasks:
        print("\nYour Tasks:")
        for task in tasks:
            print(task)
    else:
        print("\nNo tasks found.")

# Update Task Status
def update_task():
    task_id = input("Enter Task ID: ")
    status = input("Enter new status (pending/completed): ").lower()
    
    if status not in ['pending', 'completed']:
        print("Invalid status! Please enter 'pending' or 'completed'.")
        return
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tb_todo SET status=%s WHERE id=%s", (status, task_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Task updated successfully!")

# Delete Task
def delete_task():
    task_id = input("Enter Task ID: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tb_todo WHERE id=%s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Task deleted successfully!")

# Main Menu
def main():
    setup_database()

    while True:
        print("\n1) Add Task")
        print("2) View Tasks")
        print("3) Update Task Status")
        print("4) Delete Task")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting... Have a nice day!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

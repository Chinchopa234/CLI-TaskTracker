# TaskCLI - Command Line Task Manager

This is a solution for the [task-tracker project](https://roadmap.sh/projects/task-tracker) from [roadmap.sh](https://roadmap.sh)

## Features

- ✅ Add, delete, and update tasks
- 🏷️ Track task status: `todo`, `in-progress`, or `done`
- 🔍 Filter tasks by status
- 📅 Automatic timestamps for task creation and updates
- 📊 Clean tabular display of tasks

## Installation

### Using pip
```bash
pip install git+https://github.com/Chinchopa234/CLI-TaskTracker.git
```

### From source
```bash
git clone https://github.com/Chinchopa234/CLI-TaskTracker.git
cd CLI-TaskTracker
python setup.py install
```
## Usage

- **Add a task**

```bash
$ taskcli add 'Plant a tree'
Task added successfully (ID: 1)
$ taskcli add 'Build a house'
Task added successfully (ID: 2)
$ taskcli add 'Buy groceries'
Task added successfully (ID: 3)
```

- **Update a task**

```bash
$ taskcli update 3 'Raise a son'
```

- **Mark a task as done or in-progress**

```bash
$ taskcli mark-in-progress 1
$ taskcli mark-done 2
```

- **Delete a task**

```bash
$ taskcli delete 3
```

- **List all tasks**

```bash
$ taskcli list

id | description   | status      | createdAt           | updatedAt          
---+---------------+-------------+---------------------+--------------------
1  | Plant a tree  | in-progress | 21-07-2025 16-13-19 | 21-07-2025 16-14-29
2  | Build a house | done        | 21-07-2025 16-13-28 | 21-07-2025 16-14-35
```

- **Filter tasks by status**

```bash
$ taskcli list in-progress

id | description   | status      | createdAt           | updatedAt          
---+---------------+-------------+---------------------+--------------------
1  | Plant a tree  | in-progress | 21-07-2025 16-13-19 | 21-07-2025 16-14-29

$ taskcli list done

id | description   | status      | createdAt           | updatedAt          
---+---------------+-------------+---------------------+--------------------
2  | Build a house | done        | 21-07-2025 16-13-28 | 21-07-2025 16-14-35
```

#!/usr/bin/env python3
import argparse
import datetime
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Task Tracker')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add new task')
    add_parser.add_argument('task', type=str, help='Task name')

    delete_parser = subparsers.add_parser('delete', help='Delete task')
    delete_parser.add_argument('id', type=int, help='Task id')

    update_parser = subparsers.add_parser('update', help='Update task')
    update_parser.add_argument('id', type=int, help='Task id')
    update_parser.add_argument('task', type=str, help='Task name')

    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', nargs='?', default='all', choices=['all','in-progress','done'], type=str, help='Filter tasks by status')

    mark_ip_parser = subparsers.add_parser('mark-in-progress', help='Mark task as in-progress')
    mark_ip_parser.add_argument('id', type=int, help='Task id')

    mark_done_parser = subparsers.add_parser('mark-done', help='Mark task as done')
    mark_done_parser.add_argument('id', type=int, help='Task id')

    args = parser.parse_args()

    if not Path('data.json').exists():
        with open('data.json', "w") as file:
            json.dump([], file)

    match args.command:
        case 'add':
            add_task(args.task)
        case 'delete':
            delete_task(args.id)
        case 'update':
            update_task(args.id, args.task)
        case 'list':
            list_tasks(args.status)
        case 'mark-in-progress':
            update_task(args.id, new_status='in-progress')
        case 'mark-done':
            update_task(args.id, new_status='done')

def add_task(task: str):
    date = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')
    new_task = {'id': 1,
            'description': task,
            'status': 'todo',
            'createdAt': date,
            'updatedAt': date}
    with open('data.json', 'r+') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
        if data:
            ids = sorted([task['id'] for task in data])
            new_id = 1
            while new_id in ids:
                new_id += 1
            new_task['id'] = new_id
        data.append(new_task)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    print(f'Task added successfully (ID: {new_task["id"]})')

def delete_task(id_: int):
    with open('data.json', 'r+') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print('An error occurred:', e)
            return

        if not data:
            print('Task list is empty')
            return

        for task in data:
            if task['id'] == id_:
                data.remove(task)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def update_task(id_: int, new_task: str = None, new_status: str = None):
    with open('data.json', 'r+') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print('An error occurred:', e)
            return

        if not data:
            print('Task list is empty')
            return

        for task in data:
            if task['id'] == id_:
                if new_task:
                    task['description'] = new_task
                if new_status:
                    task['status'] = new_status
                date = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')
                task['updatedAt'] = date
                break

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def list_tasks(status: str = 'all'):
    with open('data.json', 'r+') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print('An error occurred:', e)
            return

    if not data:
        print('Task list is empty')
        return

    headers = ('id', 'description', 'status', 'createdAt', 'updatedAt')

    col_widths = {key: len(key) for key in headers}
    for item in data:
        for key, value in item.items():
            col_widths[key] = max(col_widths[key], len(str(value)))

    header = " | ".join(key.ljust(col_widths[key]) for key in headers)
    divider = "-+-".join("-" * col_widths[key] for key in headers)
    print(header)
    print(divider)

    data = [t for t in data if status == 'all' or t['status'] == status]
    for item in sorted(data, key=lambda task: task['id']):
        row = " | ".join(str(item.get(key, "")).ljust(col_widths[key]) for key in headers)
        print(row)

if __name__ == '__main__':
    main()
import argparse
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/tasks"]

def getCredentials() -> Credentials:
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def getList(service, title):
    results = service.tasklists().list().execute()
    items = results.get("items", [])
    for item in items:
        if item.get("title") == title:
            return item["id"]
    return None

def add(service, arg, title):
    tasklistID = getList(service, title)

    if tasklistID == None:
        print(f'List: {title} does not exist')
        return

    task = {'title': arg}
    service.tasks().insert(tasklist=tasklistID, body=task).execute()
    print(f"[{title}] Task created: {arg}")

def show(service, title):
    tasklistID = getList(service, title)

    if tasklistID == None:
        print(f'List: {title} does not exist')
        return

    results = service.tasks().list(tasklist=tasklistID).execute()
    tasks = results.get('items', [])
    print(f"List: {title}")
    for task in tasks:
        print(task.get('title'))

def main():
    creds = getCredentials()
    service = build("tasks", "v1", credentials=creds)

    try:
        if args.task:
            add(service, args.task, 'Task')
        elif args.note:
            add(service, args.note, 'Notes')
        elif args.tasks:
            show(service, 'Task')
        elif args.notes:
            show(service, 'Notes')
        else:
            print("Command not found. Use --help for usage.")
    except HttpError as err:
        print(f"Google Task API - ERROR: {err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage tasks and notes with Google Tasks")
    parser.add_argument('--task', type=str help="Add a task")
    parser.add_argument('--note', type=str help="Add a note")
    parser.add_argument('--tasks', action='store_true' help="Show tasks")
    parser.add_argument('--notes', action='store_true' help="Show notes")
    args = parser.parse_args()
    main()




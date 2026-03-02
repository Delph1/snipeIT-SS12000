from src.client.ss12000_client import SS12000Client

def main():
    client = SS12000Client()

    # Fetch users
    users = client.fetch_users(limit=10)
    print(f"Fetched {len(users)} users:")
    for user in users:
        print(f"- {user.given_name} {user.family_name} (ID: {user.id})")

    # Fetch groups for the first user
    if users:
        user_id = users[0].id
        groups = client.fetch_user_groups(user_id)
        print(f"\nGroups for user {user_id}:")
        for group in groups:
            print(f"- {group.display_name} (Type: {group.group_type})")

    # Register a webhook for Person and Group
    entities = ["Person", "Group"]
    webhook_response = client.register_webhook(entities)
    print(f"\nWebhook registered: {webhook_response}")

if __name__ == "__main__":
    main()

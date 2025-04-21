import os
import argparse
import boto3
import json



# Function to list IAM users and save output
def list_users(client, output_path):
    try:
        response = client.list_users()
        with open(output_path, "w") as f:
            f.write(json.dumps(response, indent=2, default=str))
        print(f"\033[92m[+]\033[0m Saved list of users to {output_path}")
    except Exception as e:
        error_message = f"\033[91m[!]\033[0m Error listing groups: {e}"
        print(error_message)
        with open(output_path, "w") as f:
            f.write(error_message)

# Function to list IAM groups and save output        
def list_groups(client, output_path):
    try:
        response = client.list_groups()
        with open(output_path, "w") as f:
            f.write(json.dumps(response, indent=2, default=str))
        print(f"\033[92m[+]\033[0m Saved list of groups to {output_path}")
    except Exception as e:
        error_message = f"\033[91m[!]\033[0m Error listing groups: {e}"
        print(error_message)
        with open(output_path, "w") as f:
            f.write(error_message)

# Function to list groups for a specific IAM user and save output
def list_groups_for_user(client, output_path, user_name):
    try:
        response = client.list_groups_for_user(UserName=user_name)
        with open(output_path, "w") as f:
            f.write(json.dumps(response, indent=2, default=str))
        print(f"\033[92m[+]\033[0m Saved groups for '{user_name}' to {output_path}")
    except Exception as e:
        error_message = f"\033[91m[!]\033[0m Error listing groups for user '{user_name}': {e}"
        print(error_message)
        with open(output_path, "w") as f:
            f.write(error_message)
            
# Function to list roles and save output
def list_roles(client, output_path):
    try:
        response = client.list_roles()
        with open(output_path, "w") as f:
            f.write(json.dumps(response, indent=2, default=str))
        print(f"\033[92m[+]\033[0m Saved list of roles to {output_path}")
    except Exception as e:
        error_message = f"\033[91m[!]\033[0m Error listing roles: {e}"
        print(error_message)
        with open(output_path, "w") as f:
            f.write(error_message)
            
# Function to list user policies for a specific IAM user and save output
def list_user_policies(client, output_path, user_name):
    try:
        response = client.list_user_policies(UserName=user_name)
        with open(output_path, "w") as f:
            f.write(json.dumps(response, indent=2, default=str))
        print(f"\033[92m[+]\033[0m Saved policies for '{user_name}' to {output_path}")
    except Exception as e:
        error_message = f"\033[91m[!]\033[0m Error listing policies for user '{user_name}': {e}"
        print(error_message)
        with open(output_path, "w") as f:
            f.write(error_message)
            
# Function to list attached user policies for a specific IAM user and save output
def list_attached_user_policies(client, output_path, user_name):
    try:
        response = client.list_attached_user_policies(UserName=user_name)
        with open(output_path, "w") as f:
            f.write(json.dumps(response, indent=2, default=str))
        print(f"\033[92m[+]\033[0m Saved attached policies for '{user_name}' to {output_path}")
    except Exception as e:
        error_message = f"\033[91m[!]\033[0m Error listing policies for user '{user_name}': {e}"
        print(error_message)
        with open(output_path, "w") as f:
            f.write(error_message)

def main():
    # Define CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True, help="AWS CLI profile name")
    parser.add_argument("--user-name", required=True, help="IAM user name to query")
    args = parser.parse_args()

    print(f"Using AWS profile: {args.profile}")
    print(f"Target IAM user: {args.user_name}")

    # Base directory named after the profile
    base_dir = args.profile

    # Subfolders to create
    subfolders = [
        "users", "groups", "groups-for-user",
        "roles", "user-policies"
    ]

    # Create directories
    for folder in subfolders:
        path = os.path.join(base_dir, folder)
        os.makedirs(path, exist_ok=True)
    print(f"Created folder structure under ./{base_dir}")
    
    # Create boto3 session and IAM client
    session = boto3.Session(profile_name=args.profile)
    client = session.client("iam")

    # Call list_users and save output
    user_output_file = os.path.join(base_dir, "users", "list-users.out")
    list_users(client, user_output_file)

    # Call list_groups and save output
    group_output_file = os.path.join(base_dir, "groups", "list-groups.out")
    list_groups(client, group_output_file)

    # Call list_groups_for_user and save output
    user_group_output_file = os.path.join(base_dir, "groups-for-user", "list-groups-for-user.out")
    list_groups_for_user(client, user_group_output_file, args.user_name)
    
    # Call list_roles and save output
    roles_output_file = os.path.join(base_dir, "roles", "list-roles.out")
    list_roles(client, roles_output_file)
    
    # Call list_user_policies and save out
    list_user_policies_output_file = os.path.join(base_dir, "user-policies", "list-user-policies.out")
    list_user_policies(client, list_user_policies_output_file, args.user_name)
    
    # Call list_attached_user_policies and save out
    list_attached_user_policies_output_file = os.path.join(base_dir, "user-policies", "list-attached-user-policies.out")
    list_attached_user_policies(client, list_attached_user_policies_output_file, args.user_name)

if __name__ == "__main__":
    main()

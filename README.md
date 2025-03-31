This is a Python script to help automate and organize the redundancy of common AWS IAM commands for enumeration. This script will take in a profile and a username, then perform the following AWS IAM enumeration:

- list-users
- list-groups
- list-groups-for-user
- list-roles
- list-user-policies
- list-attached-user-policies

The script will then create a directory titled by the profile you provide, then create subfolders for users,groups,groups-for-user,roles,and user-policies. From there it will save the output of the above commands to each respective subfolder for clean and easy organization

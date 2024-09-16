import configparser
import os

# Get the user's home directory and locate the .gitconfig file
gitconfig_path = os.path.expanduser("~/.gitconfig")

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the .gitconfig file if it exists
if os.path.exists(gitconfig_path):
    config.read(gitconfig_path)
else:
    print(".gitconfig file not found, creating a new configuration file...")

# Function to edit the configuration
def edit_config(section, option, value):
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)

# User input interaction function
def user_input():
    while True:
        print("\nChoose an action:")
        print("1. Edit configuration")
        print("2. Show current configuration")
        print("3. Save and exit")
        print("4. Exit without saving")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            section = input("Enter section name (e.g., user, commit, core): ").strip()
            option = input("Enter option name (e.g., name, email, gpgsign): ").strip()
            value = input("Enter value: ").strip()
            edit_config(section, option, value)
            print(f"Modified [{section}] {option} = {value}")
        elif choice == '2':
            for section in config.sections():
                print(f"[{section}]")
                for option in config[section]:
                    print(f"    {option} = {config[section][option]}")
        elif choice == '3':
            with open(gitconfig_path, 'w') as configfile:
                config.write(configfile)
            print(f"Configuration saved to {gitconfig_path}")
            break
        elif choice == '4':
            print("Exiting without saving changes.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the interaction function
user_input()

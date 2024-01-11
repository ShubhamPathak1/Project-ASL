import os

# Path for the main directory
main_dir = 'Data'

# List of actions
actions = ['Yes', 'Want']

# Create main directory if it doesn't exist
if not os.path.exists(main_dir):
    os.makedirs(main_dir)

# Create subdirectories for each action
for action in actions:
    action_dir = os.path.join(main_dir, action)
    if not os.path.exists(action_dir):
        os.makedirs(action_dir)
    
    # Create subdirectories inside each action directory
    for i in range(30):
        sub_dir = os.path.join(action_dir, str(i))
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)

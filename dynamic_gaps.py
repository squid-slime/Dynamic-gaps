#!/usr/bin/env python3
import i3ipc

try:
    import notify2
    NOTIFY_AVAILABLE = True
except ModuleNotFoundError:
    NOTIFY_AVAILABLE = False

# initialize notify2
if NOTIFY_AVAILABLE:
    notify2.init("Dynamic Gaps")

# flag to control notifications
enable_notifications = True        # CAPITALIZE first letter True False

# Define the outputs to be affected
AFFECTED_OUTPUTS = ["DP-1", "DP-2"]

def set_gaps(connection, workspace, num_windows):
    try:
        gap_size_hoz = 0         #
        gap_size_ver = 0         # leave these at 0
        gap_size_inner = 0       #

        if num_windows == 1:
            gap_size_hoz = 500      # set horizontal gaps
            gap_size_ver = 75       # set vertical gaps
            gap_size_inner = 0      # set inner gaps
        elif num_windows == 2:
            gap_size_hoz = 250
            gap_size_ver = 50
            gap_size_inner = 75
        elif num_windows == 3:
            gap_size_hoz = 100
            gap_size_ver = 75
            gap_size_inner = 50
        elif num_windows == 4:
            gap_size_hoz = 50
            gap_size_ver = 55
            gap_size_inner = 22
        elif num_windows == 5:
            gap_size_hoz = 40
            gap_size_ver = 45
            gap_size_inner = 30
        elif num_windows == 6:
            gap_size_hoz = 30
            gap_size_ver = 35
            gap_size_inner = 20
        elif num_windows == 7:
            gap_size_hoz = 25
            gap_size_ver = 25
            gap_size_inner = 20
        elif num_windows == 8:
            gap_size_hoz = 20
            gap_size_ver = 20
            gap_size_inner = 15
        elif num_windows == 9:
            gap_size_hoz = 15
            gap_size_ver = 15
            gap_size_inner = 10
        elif num_windows >= 10:
            gap_size_hoz = 10
            gap_size_ver = 10
            gap_size_inner = 10

        connection.command(f'gaps horizontal current set {gap_size_hoz}; gaps vertical current set {gap_size_ver}; gaps inner current set {gap_size_inner}')

        # display notification if enabled
        if enable_notifications and NOTIFY_AVAILABLE:
            notify2.Notification("Gaps Updated", f"Horizontal: {gap_size_hoz}, Vertical: {gap_size_ver}, Inner: {gap_size_inner}", "dialog-information").show()
    except Exception as e:
        error_message = f"An error occurred while setting gaps: {e}"
        if NOTIFY_AVAILABLE:
            notify2.Notification("Error", error_message, "dialog-error").show()
        else:
            print(error_message)

def get_output_of_workspace(workspace):
    while workspace:
        if workspace.type == 'output':
            return workspace.name
        workspace = workspace.parent
    return None

def update_gaps(connection, event=None):
    try:
        current_workspace = connection.get_tree().find_focused().workspace()
        current_output = get_output_of_workspace(current_workspace)
        if current_output in AFFECTED_OUTPUTS:
            num_windows = len([node for node in current_workspace.leaves() if not node.floating])
            set_gaps(connection, current_workspace.name, num_windows)
    except Exception as e:
        error_message = f"An error occurred: {e}"
        if NOTIFY_AVAILABLE:
            notify2.Notification("Error", error_message, "dialog-error").show()
        else:
            print(error_message)

def main():
    try:
        connection = i3ipc.Connection()
        connection.on('window::new', update_gaps)
        connection.on('window::close', update_gaps)
        connection.on('workspace::focus', update_gaps)
        connection.main()
    except Exception as e:
        error_message = f"An error occurred: {e}"
        if NOTIFY_AVAILABLE:
            notify2.Notification("Error", error_message, "dialog-error").show()
        else:
            print(error_message)

if __name__ == '__main__':
    main()

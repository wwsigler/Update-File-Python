
# Python script to update the allow list based on a remove list

def update_allow_list(allow_file, remove_list):
    """ 
    This function updates the allow list by removing IPs that are present in the remove list.
    
    Parameters:
    allow_file (str): The filename of the allow list.
    remove_list (list): The list of IPs to remove from the allow list.
    
    """
    
    # Step 1: Open the file containing the allow list
    with open(allow_file, 'r') as file:
        ip_addresses = file.read().splitlines()  # Read the contents and split into a list
    
    # Step 2: Iterate through the remove list and remove matching IPs
    for ip in remove_list:
        if ip in ip_addresses:
            ip_addresses.remove(ip)  # Remove the IP address if found
    
    # Step 3: Update the allow list file with the revised list of IPs
    with open(allow_file, 'w') as file:
        file.write("\n".join(ip_addresses))  # Write the updated list back to the file


if __name__ == "__main__":
    # Example usage of the update_allow_list function
    
    # Sample allow list file (this should be the actual file path in practice)
    allow_list_file = 'allow_list.txt'
    
    # Sample remove list of IP addresses to remove
    remove_ips = [
        '192.168.1.10',
        '192.168.1.20',
        '192.168.1.30'
    ]
    
    # Call the function to update the allow list
    update_allow_list(allow_list_file, remove_ips)
    
    print(f"Updated the allow list in {allow_list_file} by removing IPs from the remove list.")

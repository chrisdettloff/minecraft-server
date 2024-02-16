import datetime
import os

from google.cloud import compute_v1

# Set your Google Cloud project ID
project_id = "YOUR_PROJECT_ID" 

def make_firewall_rule(request):
    """HTTP Cloud Function to create a Minecraft firewall rule."""

    # Get the caller's IP address (Adapt if not using an HTTP Cloud Function)
    if 'X-Forwarded-For' in request.headers:
        caller_ip = request.headers['X-Forwarded-For']
    else:
        caller_ip = request.remote_addr  # Assumes a direct call

    # Generate a unique firewall rule name
    timestamp = datetime.datetime.now().timestamp()
    firewall_name = f'minecraft-fw-rule-{int(timestamp)}'

    # Firewall configuration
    config = {
        'protocols': {'tcp': [25565]}, 
        'allowed': [{'IPProtocol': 'tcp', 'ports': ['25565']}],
        'source_ranges': [f'{caller_ip}/32'],
        'target_tags': ['minecraft-server'], 
    }
   
    # Create the Compute Engine client
    compute_client = compute_v1.FirewallsClient()

    # Create the firewall rule
    operation = compute_client.insert(project=project_id, firewall_resource=config)

    # Simplified handling compared to Node.js, would usually wait for operation completion 
    operation.result()  

    return f'Firewall rule created named {firewall_name} for IP address {caller_ip}', 200 

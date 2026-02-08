import os
import requests
import csv
import io
import random
import hashlib
from django.shortcuts import render

# Placeholder for Google Sheets CSV URL
# You can replace this with the actual URL from the user or configuration

# Placeholder for the Google Sheet URL
GOOGLE_SHEET_CSV_URL = os.getenv('GSHEET_URL')

import hashlib

def generate_tech_alias(name):
    # Normalize the name to handle accidental spaces or case changes
    clean_name = name.strip().lower()
    suffixes = [".sh", ".exe", "_v2.0", "0x_dev", ".py"]
    
    # Generate a stable number from the name using MD5
    # This number will NEVER change for the same string
    name_hash = hashlib.md5(clean_name.encode()).hexdigest()
    hash_int = int(name_hash, 16)
    
    # Use the hash to pick a suffix consistently
    chosen_suffix = suffixes[hash_int % len(suffixes)]
    
    return f"{clean_name}{chosen_suffix}"

def generate_avatar_url(alias):
    # Use the alias directly as the seed for DiceBear
    # No extra hashing needed if the alias is already stable
    return f"https://api.dicebear.com/9.x/bottts/svg?seed={alias}"

def get_dashboard_data(request):
    """
    Fetches data from Google Sheet, transforms it, and renders the dashboard.
    """
    participants = []
    
    # Easter egg: 'import antigravity'
    # This is a nod to the classic Python XKCD comic and module.
    # https://xkcd.com/353/
    # import antigravity  <-- Uncommenting this would open the comic! 

    try:
        # In a real scenario, we would stream this or cache it
        response = requests.get(GOOGLE_SHEET_CSV_URL)
        response.raise_for_status()
        
        # Decode content and parse CSV
        csv_content = response.content.decode('utf-8')
        csv_reader = csv.DictReader(io.StringIO(csv_content))
        
        for row in csv_reader:
            # Assuming columns like 'Name', 'Role', 'Domain' exist. 
            # Adapt keys based on actual CSV structure.
            name = row.get('Name', 'Unknown User')
            role = row.get('Role', 'Participant')
            domain = row.get('Domain', 'Tech')
            
            alias = generate_tech_alias(name)
            avatar_url = generate_avatar_url(alias)
            
            participants.append({
                'name': name,
                'alias': alias,
                'avatar': avatar_url,
                'role': role,
                'domain': domain,
            })
            
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        # Fallback data for demonstration/sanity check if fetch fails
        participants = [
            {'name': 'Alice Smith', 'alias': 'alice.sh', 'avatar': generate_avatar_url('alice.sh'), 'role': 'Frontend', 'domain': 'Web'},
            {'name': 'Bob Jones', 'alias': '0xbob', 'avatar': generate_avatar_url('0xbob'), 'role': 'Backend', 'domain': 'Cloud'},
             {'name': 'Charlie Day', 'alias': 'sudo_charlie', 'avatar': generate_avatar_url('sudo_charlie'), 'role': 'Designer', 'domain': 'UI/UX'},
        ]

    return render(request, 'dashboard/index.html', {'participants': participants})

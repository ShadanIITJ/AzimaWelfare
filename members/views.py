from django.shortcuts import render
import os
import json
from django.conf import settings

def members_list(request):
    members_file = os.path.join(settings.BASE_DIR, 'members', 'members.json')
    members = []
    if os.path.exists(members_file):
        with open(members_file, 'r', encoding='utf-8') as f:
            members = json.load(f)
    return render(request, 'members/members_list.html', {'members': members})

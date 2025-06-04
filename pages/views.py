from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

import os
import json
from django.conf import settings

def gallery(request):
    events_dir = os.path.join(settings.MEDIA_ROOT, 'events')
    gallery_images = []
    
    if os.path.exists(events_dir):
        for event_folder in os.listdir(events_dir):
            event_path = os.path.join(events_dir, event_folder)
            json_path = os.path.join(event_path, 'event.json')
            
            if os.path.isdir(event_path) and os.path.exists(json_path):
                try:
                    # Read event details
                    with open(json_path, 'r') as f:
                        event_data = json.load(f)
                    
                    # Get all images from the event folder
                    for file in os.listdir(event_path):
                        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                            gallery_images.append({
                                'url': f'/media/events/{event_folder}/{file}',
                                'event_name': event_data.get('name', event_folder.replace('_', ' ').title()),
                                'date': event_data.get('date', ''),
                                'location': event_data.get('location', ''),
                                'event_url': f'/events/{event_folder}/'
                            })
                except:
                    continue    # Sort images by event date in descending order
    gallery_images.sort(key=lambda x: x['date'], reverse=True)
    
    return render(request, 'pages/gallery.html', {
        'gallery_images': gallery_images
    })

def donation(request):
    return render(request, 'pages/donation.html')

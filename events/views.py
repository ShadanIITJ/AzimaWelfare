from django.shortcuts import render
import os
from django.conf import settings

def event_list(request):
    events_dir = os.path.join(settings.MEDIA_ROOT, 'events')
    events = []
    if os.path.exists(events_dir):
        for event_folder in os.listdir(events_dir):
            event_path = os.path.join(events_dir, event_folder)
            if os.path.isdir(event_path):
                events.append({
                    'slug': event_folder,
                    'name': event_folder.replace('_', ' ').title(),
                })
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_slug):
    event_path = os.path.join(settings.MEDIA_ROOT, 'events', event_slug)
    images = []
    if os.path.exists(event_path):
        for file in os.listdir(event_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(f'/media/events/{event_slug}/{file}')
    return render(request, 'events/event_detail.html', {
        'event_slug': event_slug,
        'images': images,
    })

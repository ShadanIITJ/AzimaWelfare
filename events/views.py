from django.shortcuts import render
import os
import json
from django.conf import settings
from django.http import Http404

def get_event_cover_image(event_folder, event_data):
    """Helper function to get a cover image for an event"""
    events_dir = os.path.join(settings.MEDIA_ROOT, 'events')
    event_path = os.path.join(events_dir, event_folder)
    
    # First try to use specified cover image
    if event_data.get("cover_image"):
        cover_path = os.path.join(event_path, event_data["cover_image"])
        if os.path.exists(cover_path):
            return f'/media/events/{event_folder}/{event_data["cover_image"]}'
    
    # If no cover image or it doesn't exist, pick first image from folder
    for file in os.listdir(event_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return f'/media/events/{event_folder}/{file}'
    
    # If no images found, return None
    return None

def event_list(request):
    events_dir = os.path.join(settings.MEDIA_ROOT, 'events')
    events = []
    if os.path.exists(events_dir):
        for event_folder in os.listdir(events_dir):
            event_path = os.path.join(events_dir, event_folder)
            json_path = os.path.join(event_path, 'event.json')
            
            if os.path.isdir(event_path) and os.path.exists(json_path):
                try:
                    with open(json_path, 'r') as f:
                        event_data = json.load(f)
                        
                    # Count images in the event folder
                    image_count = sum(1 for file in os.listdir(event_path) 
                                   if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')))
                        
                    events.append({
                            'slug': event_folder,
                            'name': event_data.get('name', event_folder.replace('_', ' ').title()),
                            'date': event_data.get('date', ''),
                            'location': event_data.get('location', ''),
                            'description': event_data.get('description', '')[:100] + '...' if len(event_data.get('description', '')) > 100 else event_data.get('description', ''),
                            'cover_image': get_event_cover_image(event_folder, event_data),
                            'image_count': image_count
                        })
                except:
                    continue
              # Sort events by date, most recent first
        events.sort(key=lambda x: x['date'], reverse=True)
                    
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_slug):
    event_path = os.path.join(settings.MEDIA_ROOT, 'events', event_slug)
    json_path = os.path.join(event_path, 'event.json')
    
    if not os.path.exists(event_path) or not os.path.exists(json_path):
        raise Http404("Event not found")
        
    # Load event details from JSON
    try:
        with open(json_path, 'r') as f:
            event_data = json.load(f)
    except:
        raise Http404("Event data is invalid")
    
    # Get cover image
    cover_image = get_event_cover_image(event_slug, event_data)
      # Get all images from the event folder
    images = []
    
    if os.path.exists(event_path):
        for file in os.listdir(event_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append({
                    'url': f'/media/events/{event_slug}/{file}',
                    'title': file.rsplit('.', 1)[0].replace('_', ' ').title()
                })
    
    return render(request, 'events/event_detail.html', {
        'event': {
            'slug': event_slug,
            'name': event_data.get('name', event_slug.replace('_', ' ').title()),
            'date': event_data.get('date', ''),
            'description': event_data.get('description', ''),
            'cover_image': cover_image,
            'location': event_data.get('location', ''),
            'organizer': event_data.get('organizer', '')
        },
        'images': images
    })

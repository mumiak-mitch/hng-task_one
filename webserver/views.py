from django.http import JsonResponse
from django.conf import settings
import ipinfo

def visitor_greeting(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')  # Use '127.0.0.1' for local testing
    
    # Fetching location based on IP (using ipinfo service)
    location = get_location(client_ip)
    
    greeting = f"Hello, {visitor_name}! The temperature is 11 degrees Celsius in {location}."
    
    data = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }
    
    return JsonResponse(data)

def get_location(ip):
    ipinfo_token = getattr(settings, "IPINFO_TOKEN", None)
    ipinfo_settings = getattr(settings, "IPINFO_SETTINGS", {})
    
    if not ipinfo_token:
        print("Error: IPINFO_TOKEN is not set in environment variables.")
        return 'Unknown'
    
    handler = ipinfo.getHandler(ipinfo_token, **ipinfo_settings)
    ip_data = handler.getDetails(ip)
    
    if ip_data:
        return ip_data.all.get('city', 'Unknown')
    else:
        return 'Unknown'

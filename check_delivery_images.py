#!/usr/bin/env python
"""
Script to query tracking records for delivery images
Usage: python check_delivery_images.py [tracking_number]

This script connects to the Karrio database and searches for tracking records
that have delivery_image or signature_image data.
"""

import os
import sys
import django
from pathlib import Path

# Add the project path to sys.path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / 'apps' / 'api'))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karrio.server.settings')
django.setup()

# Now import Django models
from karrio.server.manager.models import Tracking


def search_tracking_with_images(tracking_number=None):
    """
    Search for tracking records with delivery images.
    
    Args:
        tracking_number (str, optional): Specific tracking number to search for
        
    Returns:
        QuerySet of tracking records with delivery images
    """
    # Base query for records that have delivery images
    query = Tracking.objects.exclude(
        delivery_image__isnull=True, 
        signature_image__isnull=True
    ).exclude(
        delivery_image='', 
        signature_image=''
    )
    
    # Filter by specific tracking number if provided
    if tracking_number:
        query = query.filter(tracking_number=tracking_number)
    
    return query


def display_tracking_info(tracking_records):
    """Display tracking record information in a readable format"""
    
    if not tracking_records.exists():
        print("No tracking records found with delivery images.")
        return
    
    print(f"\nFound {tracking_records.count()} tracking record(s) with delivery images:\n")
    print("-" * 80)
    
    for track in tracking_records:
        print(f"Tracking ID: {track.id}")
        print(f"Tracking Number: {track.tracking_number}")
        print(f"Carrier: {track.carrier_name} ({track.carrier_id})")
        print(f"Status: {track.status}")
        print(f"Delivered: {track.delivered}")
        print(f"Estimated Delivery: {track.estimated_delivery}")
        print(f"Created: {track.created_at}")
        
        # Check for delivery image
        if track.delivery_image:
            print(f"✓ Has Delivery Image: {len(track.delivery_image)} characters")
            print(f"  Delivery Image URL: {track.delivery_image_url}")
        else:
            print("✗ No Delivery Image")
            
        # Check for signature image  
        if track.signature_image:
            print(f"✓ Has Signature Image: {len(track.signature_image)} characters")
            print(f"  Signature Image URL: {track.signature_image_url}")
        else:
            print("✗ No Signature Image")
            
        # Show some tracking info
        if track.info:
            print(f"Additional Info: {track.info}")
            
        # Show recent events
        if track.events:
            latest_event = track.events[0] if track.events else None
            if latest_event:
                print(f"Latest Event: {latest_event.get('description', 'N/A')} "
                      f"on {latest_event.get('date', 'N/A')}")
        
        print("-" * 80)


def query_specific_tracking(tracking_number):
    """Query for a specific tracking number"""
    print(f"Searching for tracking number: {tracking_number}")
    
    # First check if the tracking number exists at all
    all_tracking = Tracking.objects.filter(tracking_number=tracking_number)
    if not all_tracking.exists():
        print(f"❌ No tracking record found for tracking number: {tracking_number}")
        return
    
    print(f"✓ Found tracking record for: {tracking_number}")
    
    # Now check for images
    tracking_with_images = search_tracking_with_images(tracking_number)
    
    if tracking_with_images.exists():
        display_tracking_info(tracking_with_images)
    else:
        print(f"❌ Tracking number {tracking_number} exists but has no delivery images.")
        
        # Show basic info about the tracking record
        track = all_tracking.first()
        print(f"\nBasic tracking info:")
        print(f"  Status: {track.status}")
        print(f"  Delivered: {track.delivered}")
        print(f"  Carrier: {track.carrier_name}")
        print(f"  Events count: {len(track.events) if track.events else 0}")


def query_all_with_images():
    """Query for all tracking records with delivery images"""
    print("Searching for all tracking records with delivery images...")
    
    tracking_records = search_tracking_with_images()
    display_tracking_info(tracking_records)


def get_statistics():
    """Get statistics about tracking records"""
    total_tracking = Tracking.objects.count()
    with_delivery_images = Tracking.objects.exclude(delivery_image__isnull=True).exclude(delivery_image='').count()
    with_signature_images = Tracking.objects.exclude(signature_image__isnull=True).exclude(signature_image='').count()
    with_any_images = Tracking.objects.exclude(
        delivery_image__isnull=True, 
        signature_image__isnull=True
    ).exclude(
        delivery_image='', 
        signature_image=''
    ).count()
    
    print(f"\n📊 Tracking Records Statistics:")
    print(f"  Total tracking records: {total_tracking}")
    print(f"  With delivery images: {with_delivery_images}")
    print(f"  With signature images: {with_signature_images}")
    print(f"  With any images: {with_any_images}")
    print(f"  Percentage with images: {(with_any_images/total_tracking)*100:.1f}%" if total_tracking > 0 else "  No tracking records found")


def main():
    """Main function to handle command line arguments"""
    
    if len(sys.argv) > 1:
        tracking_number = sys.argv[1]
        if tracking_number.lower() in ['--stats', '-s']:
            get_statistics()
        elif tracking_number.lower() in ['--all', '-a']:
            query_all_with_images()
        else:
            query_specific_tracking(tracking_number)
    else:
        print("Karrio Delivery Image Checker")
        print("=" * 40)
        get_statistics()
        print("\n" + "=" * 40)
        query_all_with_images()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        print("\nUsage:")
        print("  python check_delivery_images.py                    # Show stats and all records with images")
        print("  python check_delivery_images.py <tracking_number>  # Check specific tracking number")
        print("  python check_delivery_images.py --stats           # Show statistics only")
        print("  python check_delivery_images.py --all             # Show all records with images")
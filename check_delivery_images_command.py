"""
Django management command to check delivery images in tracking records.

Add this to: apps/api/karrio/server/manager/management/commands/check_delivery_images.py
Then run: python manage.py check_delivery_images
"""

from django.core.management.base import BaseCommand
from karrio.server.manager.models import Tracking


class Command(BaseCommand):
    help = 'Check tracking records for delivery images'

    def add_arguments(self, parser):
        parser.add_argument(
            '--tracking-number',
            type=str,
            help='Check a specific tracking number',
        )
        parser.add_argument(
            '--stats-only',
            action='store_true',
            help='Show only statistics',
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=20,
            help='Limit the number of results shown (default: 20)',
        )

    def handle(self, *args, **options):
        tracking_number = options.get('tracking_number')
        stats_only = options.get('stats_only')
        limit = options.get('limit')

        self.stdout.write(
            self.style.SUCCESS('Karrio Delivery Image Checker')
        )
        self.stdout.write('=' * 40)

        # Show statistics
        self.show_statistics()

        if stats_only:
            return

        self.stdout.write('\n' + '=' * 40)

        if tracking_number:
            self.check_specific_tracking(tracking_number)
        else:
            self.show_all_with_images(limit)

    def show_statistics(self):
        """Show statistics about tracking records with images"""
        total_tracking = Tracking.objects.count()
        with_delivery_images = Tracking.objects.exclude(
            delivery_image__isnull=True
        ).exclude(delivery_image='').count()
        
        with_signature_images = Tracking.objects.exclude(
            signature_image__isnull=True
        ).exclude(signature_image='').count()
        
        with_any_images = Tracking.objects.exclude(
            delivery_image__isnull=True, 
            signature_image__isnull=True
        ).exclude(
            delivery_image='', 
            signature_image=''
        ).count()

        self.stdout.write(f'\n📊 Statistics:')
        self.stdout.write(f'  Total tracking records: {total_tracking}')
        self.stdout.write(f'  With delivery images: {with_delivery_images}')
        self.stdout.write(f'  With signature images: {with_signature_images}')
        self.stdout.write(f'  With any images: {with_any_images}')
        
        if total_tracking > 0:
            percentage = (with_any_images / total_tracking) * 100
            self.stdout.write(f'  Percentage with images: {percentage:.1f}%')

    def check_specific_tracking(self, tracking_number):
        """Check a specific tracking number"""
        self.stdout.write(f'\nSearching for tracking number: {tracking_number}')

        # Check if tracking number exists
        all_tracking = Tracking.objects.filter(tracking_number=tracking_number)
        if not all_tracking.exists():
            self.stdout.write(
                self.style.ERROR(f'❌ No tracking record found for: {tracking_number}')
            )
            return

        self.stdout.write(
            self.style.SUCCESS(f'✓ Found tracking record for: {tracking_number}')
        )

        # Check for images
        tracking_with_images = Tracking.objects.filter(
            tracking_number=tracking_number
        ).exclude(
            delivery_image__isnull=True, 
            signature_image__isnull=True
        ).exclude(
            delivery_image='', 
            signature_image=''
        )

        if tracking_with_images.exists():
            self.display_tracking_details(tracking_with_images)
        else:
            self.stdout.write(
                self.style.WARNING(f'❌ No delivery images found for: {tracking_number}')
            )
            
            # Show basic info
            track = all_tracking.first()
            self.stdout.write('\nBasic tracking info:')
            self.stdout.write(f'  Status: {track.status}')
            self.stdout.write(f'  Delivered: {track.delivered}')
            self.stdout.write(f'  Carrier: {track.carrier_name}')
            events_count = len(track.events) if track.events else 0
            self.stdout.write(f'  Events count: {events_count}')

    def show_all_with_images(self, limit):
        """Show all tracking records with images"""
        tracking_records = Tracking.objects.exclude(
            delivery_image__isnull=True, 
            signature_image__isnull=True
        ).exclude(
            delivery_image='', 
            signature_image=''
        ).order_by('-created_at')[:limit]

        if not tracking_records:
            self.stdout.write('No tracking records found with delivery images.')
            return

        self.stdout.write(f'\nShowing {len(tracking_records)} most recent records with images:')
        self.display_tracking_details(tracking_records)

    def display_tracking_details(self, tracking_records):
        """Display detailed information about tracking records"""
        for track in tracking_records:
            self.stdout.write('\n' + '-' * 80)
            self.stdout.write(f'Tracking ID: {track.id}')
            self.stdout.write(f'Tracking Number: {track.tracking_number}')
            self.stdout.write(f'Carrier: {track.carrier_name} ({track.carrier_id})')
            self.stdout.write(f'Status: {track.status}')
            self.stdout.write(f'Delivered: {track.delivered}')
            self.stdout.write(f'Estimated Delivery: {track.estimated_delivery}')
            self.stdout.write(f'Created: {track.created_at}')

            # Check delivery image
            if track.delivery_image:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Has Delivery Image: {len(track.delivery_image)} characters'
                    )
                )
                if hasattr(track, 'delivery_image_url'):
                    self.stdout.write(f'  Delivery Image URL: {track.delivery_image_url}')
            else:
                self.stdout.write('✗ No Delivery Image')

            # Check signature image
            if track.signature_image:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Has Signature Image: {len(track.signature_image)} characters'
                    )
                )
                if hasattr(track, 'signature_image_url'):
                    self.stdout.write(f'  Signature Image URL: {track.signature_image_url}')
            else:
                self.stdout.write('✗ No Signature Image')

            # Show additional info
            if track.info:
                info_keys = list(track.info.keys())[:3]  # Show first 3 keys
                self.stdout.write(f'Additional Info keys: {", ".join(info_keys)}')

            # Show latest event
            if track.events:
                latest_event = track.events[0]
                description = latest_event.get('description', 'N/A')
                date = latest_event.get('date', 'N/A')
                self.stdout.write(f'Latest Event: {description} on {date}')

        self.stdout.write('-' * 80)
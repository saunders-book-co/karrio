# PowerShell script to check delivery images in Karrio database
# Usage: .\check_delivery_images.ps1 [tracking_number]

param(
    [string]$TrackingNumber = "",
    [switch]$Stats,
    [switch]$All,
    [switch]$SQL
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = $scriptDir

Write-Host "Karrio Delivery Image Checker" -ForegroundColor Green
Write-Host "=============================" -ForegroundColor Green

# Check if we're in the right directory
if (-not (Test-Path "$projectRoot\manage.py") -and -not (Test-Path "$projectRoot\apps\api\manage.py")) {
    Write-Error "Could not find manage.py. Make sure you're running this from the Karrio project root."
    exit 1
}

# Find the manage.py file
$managePy = ""
if (Test-Path "$projectRoot\manage.py") {
    $managePy = "$projectRoot\manage.py"
} elseif (Test-Path "$projectRoot\apps\api\manage.py") {
    $managePy = "$projectRoot\apps\api\manage.py"
}

if ($SQL) {
    # Show SQL option
    Write-Host "`nSQL Queries are available in: query_delivery_images.sql" -ForegroundColor Yellow
    Write-Host "You can run these directly against your database." -ForegroundColor Yellow
    
    # Try to detect database type and show connection info
    if (Test-Path "$projectRoot\.env") {
        Write-Host "`nDetected .env file. Database configuration:" -ForegroundColor Cyan
        Get-Content "$projectRoot\.env" | Where-Object { $_ -match "DATABASE" } | ForEach-Object {
            Write-Host "  $_" -ForegroundColor Gray
        }
    }
    
    if (Test-Path "$projectRoot\docker\.env") {
        Write-Host "`nDetected docker/.env file. Database configuration:" -ForegroundColor Cyan
        Get-Content "$projectRoot\docker\.env" | Where-Object { $_ -match "DATABASE" } | ForEach-Object {
            Write-Host "  $_" -ForegroundColor Gray
        }
    }
    
    Write-Host "`nExample PostgreSQL connection:" -ForegroundColor Cyan
    Write-Host "  psql -h localhost -U karrio -d karrio" -ForegroundColor Gray
    Write-Host "`nExample SQLite connection:" -ForegroundColor Cyan
    Write-Host "  sqlite3 db.sqlite3" -ForegroundColor Gray
    
    exit 0
}

# Check for Python virtual environment
$pythonCmd = "python"
if ($env:VIRTUAL_ENV) {
    Write-Host "Using Python virtual environment: $env:VIRTUAL_ENV" -ForegroundColor Green
} else {
    Write-Host "No virtual environment detected. You may need to activate one." -ForegroundColor Yellow
}

# Create a Django management command inline
$djangoScript = @"
import os
import sys
import django
from pathlib import Path

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karrio.server.settings')

try:
    django.setup()
    
    from karrio.server.manager.models import Tracking
    
    def search_tracking_with_images(tracking_number=None):
        query = Tracking.objects.exclude(
            delivery_image__isnull=True, 
            signature_image__isnull=True
        ).exclude(
            delivery_image='', 
            signature_image=''
        )
        
        if tracking_number:
            query = query.filter(tracking_number=tracking_number)
        
        return query
    
    def get_statistics():
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
        
        print(f'Total tracking records: {total_tracking}')
        print(f'With delivery images: {with_delivery_images}')
        print(f'With signature images: {with_signature_images}')
        print(f'With any images: {with_any_images}')
        if total_tracking > 0:
            print(f'Percentage with images: {(with_any_images/total_tracking)*100:.1f}%')
    
    def display_tracking_info(tracking_records):
        if not tracking_records.exists():
            print('No tracking records found with delivery images.')
            return
        
        print(f'Found {tracking_records.count()} tracking record(s) with delivery images:')
        print('-' * 80)
        
        for track in tracking_records[:10]:  # Limit to first 10
            print(f'Tracking ID: {track.id}')
            print(f'Tracking Number: {track.tracking_number}')
            print(f'Carrier: {track.carrier_name} ({track.carrier_id})')
            print(f'Status: {track.status}')
            print(f'Delivered: {track.delivered}')
            print(f'Created: {track.created_at}')
            
            if track.delivery_image:
                print(f'✓ Has Delivery Image: {len(track.delivery_image)} characters')
                if hasattr(track, 'delivery_image_url'):
                    print(f'  Delivery Image URL: {track.delivery_image_url}')
            else:
                print('✗ No Delivery Image')
                
            if track.signature_image:
                print(f'✓ Has Signature Image: {len(track.signature_image)} characters')
                if hasattr(track, 'signature_image_url'):
                    print(f'  Signature Image URL: {track.signature_image_url}')
            else:
                print('✗ No Signature Image')
            
            print('-' * 80)
    
    # Main execution
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == '--stats':
            get_statistics()
        elif action == '--all':
            tracking_records = search_tracking_with_images()
            display_tracking_info(tracking_records)
        else:
            # Treat as tracking number
            tracking_number = action
            print(f'Searching for tracking number: {tracking_number}')
            
            all_tracking = Tracking.objects.filter(tracking_number=tracking_number)
            if not all_tracking.exists():
                print(f'❌ No tracking record found for tracking number: {tracking_number}')
            else:
                print(f'✓ Found tracking record for: {tracking_number}')
                tracking_with_images = search_tracking_with_images(tracking_number)
                
                if tracking_with_images.exists():
                    display_tracking_info(tracking_with_images)
                else:
                    print(f'❌ Tracking number {tracking_number} exists but has no delivery images.')
                    track = all_tracking.first()
                    print(f'Status: {track.status}')
                    print(f'Delivered: {track.delivered}')
                    print(f'Carrier: {track.carrier_name}')
                    print(f'Events count: {len(track.events) if track.events else 0}')
    else:
        get_statistics()
        print()
        tracking_records = search_tracking_with_images()
        display_tracking_info(tracking_records)
        
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
"@

# Write the script to a temporary file
$tempScript = "$env:TEMP\karrio_delivery_check.py"
$djangoScript | Out-File -FilePath $tempScript -Encoding utf8

try {
    # Change to the appropriate directory
    if (Test-Path "$projectRoot\apps\api\manage.py") {
        Set-Location "$projectRoot\apps\api"
    } else {
        Set-Location $projectRoot
    }
    
    # Build arguments for the Python script
    $args = @()
    if ($Stats) {
        $args += "--stats"
    } elseif ($All) {
        $args += "--all"
    } elseif ($TrackingNumber -ne "") {
        $args += $TrackingNumber
    }
    
    # Run the Django script
    if ($args.Count -gt 0) {
        & $pythonCmd $tempScript $args
    } else {
        & $pythonCmd $tempScript
    }
    
} catch {
    Write-Error "Failed to run Django script: $_"
    Write-Host "`nTrying alternative approach..." -ForegroundColor Yellow
    
    # Try using Django management shell
    Write-Host "You can also try running these commands manually:" -ForegroundColor Cyan
    Write-Host "1. Activate your Python environment" -ForegroundColor Gray
    Write-Host "2. cd to the API directory: cd apps/api" -ForegroundColor Gray
    Write-Host "3. Run: python manage.py shell" -ForegroundColor Gray
    Write-Host "4. Execute:" -ForegroundColor Gray
    Write-Host "   from karrio.server.manager.models import Tracking" -ForegroundColor Gray
    Write-Host "   Tracking.objects.exclude(delivery_image__isnull=True).count()" -ForegroundColor Gray
    
} finally {
    # Clean up temp file
    if (Test-Path $tempScript) {
        Remove-Item $tempScript
    }
}

Write-Host "`nFor direct SQL access, run: .\check_delivery_images.ps1 -SQL" -ForegroundColor Green
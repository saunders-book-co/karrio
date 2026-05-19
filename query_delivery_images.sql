-- SQL queries to find tracking records with delivery images
-- Run these directly against your Karrio database

-- 1. Get statistics about tracking records with images
SELECT 
    COUNT(*) as total_tracking_records,
    COUNT(CASE WHEN delivery_image IS NOT NULL AND delivery_image != '' THEN 1 END) as with_delivery_image,
    COUNT(CASE WHEN signature_image IS NOT NULL AND signature_image != '' THEN 1 END) as with_signature_image,
    COUNT(CASE WHEN (delivery_image IS NOT NULL AND delivery_image != '') 
                 OR (signature_image IS NOT NULL AND signature_image != '') THEN 1 END) as with_any_image
FROM "tracking-status";

-- 2. Find all tracking records with delivery images
SELECT 
    id,
    tracking_number,
    status,
    delivered,
    estimated_delivery,
    created_at,
    CASE WHEN delivery_image IS NOT NULL AND delivery_image != '' THEN 'YES' ELSE 'NO' END as has_delivery_image,
    CASE WHEN signature_image IS NOT NULL AND signature_image != '' THEN 'YES' ELSE 'NO' END as has_signature_image,
    CASE WHEN delivery_image IS NOT NULL AND delivery_image != '' THEN LENGTH(delivery_image) END as delivery_image_size,
    CASE WHEN signature_image IS NOT NULL AND signature_image != '' THEN LENGTH(signature_image) END as signature_image_size
FROM "tracking-status" 
WHERE (delivery_image IS NOT NULL AND delivery_image != '') 
   OR (signature_image IS NOT NULL AND signature_image != '')
ORDER BY created_at DESC;

-- 3. Find specific tracking number with delivery images
-- Replace 'YOUR_TRACKING_NUMBER' with the actual tracking number you're looking for
SELECT 
    id,
    tracking_number,
    status,
    delivered,
    estimated_delivery,
    created_at,
    delivery_image IS NOT NULL AND delivery_image != '' as has_delivery_image,
    signature_image IS NOT NULL AND signature_image != '' as has_signature_image,
    info,
    events
FROM "tracking-status" 
WHERE tracking_number = 'YOUR_TRACKING_NUMBER';

-- 4. Get tracking records with delivery images and their carrier info
SELECT 
    t.id,
    t.tracking_number,
    t.status,
    t.delivered,
    t.estimated_delivery,
    t.created_at,
    CASE WHEN t.delivery_image IS NOT NULL AND t.delivery_image != '' THEN 'YES' ELSE 'NO' END as has_delivery_image,
    CASE WHEN t.signature_image IS NOT NULL AND t.signature_image != '' THEN 'YES' ELSE 'NO' END as has_signature_image,
    -- Note: You might need to join with the carrier table to get carrier details
    t.tracking_carrier_id
FROM "tracking-status" t
WHERE (t.delivery_image IS NOT NULL AND t.delivery_image != '') 
   OR (t.signature_image IS NOT NULL AND t.signature_image != '')
ORDER BY t.created_at DESC
LIMIT 20;

-- 5. Count tracking records by carrier that have delivery images
SELECT 
    tracking_carrier_id,
    COUNT(*) as records_with_images,
    COUNT(CASE WHEN delivery_image IS NOT NULL AND delivery_image != '' THEN 1 END) as with_delivery_image,
    COUNT(CASE WHEN signature_image IS NOT NULL AND signature_image != '' THEN 1 END) as with_signature_image
FROM "tracking-status" 
WHERE (delivery_image IS NOT NULL AND delivery_image != '') 
   OR (signature_image IS NOT NULL AND signature_image != '')
GROUP BY tracking_carrier_id
ORDER BY records_with_images DESC;

-- 6. Get the actual delivery image data (be careful - this might return large text fields)
-- Only run this for specific tracking numbers you're interested in
SELECT 
    id,
    tracking_number,
    delivery_image,
    signature_image
FROM "tracking-status" 
WHERE tracking_number = 'YOUR_TRACKING_NUMBER'
  AND ((delivery_image IS NOT NULL AND delivery_image != '') 
       OR (signature_image IS NOT NULL AND signature_image != ''));

-- 7. Recently delivered packages with images
SELECT 
    t.id,
    t.tracking_number,
    t.estimated_delivery,
    t.delivered,
    CASE WHEN t.delivery_image IS NOT NULL AND t.delivery_image != '' THEN 'YES' ELSE 'NO' END as has_delivery_image,
    CASE WHEN t.signature_image IS NOT NULL AND t.signature_image != '' THEN 'YES' ELSE 'NO' END as has_signature_image
FROM "tracking-status" t
WHERE t.delivered = true
  AND ((t.delivery_image IS NOT NULL AND t.delivery_image != '') 
       OR (t.signature_image IS NOT NULL AND t.signature_image != ''))
  AND t.estimated_delivery >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY t.estimated_delivery DESC;
{{ config(materialized='table') }}

SELECT
    month,
    town,
    flat_type,
    block,
    street_name,
    storey_range,
    CAST(floor_area_sqm AS NUMERIC) AS floor_area_sqm,
    flat_model,
    lease_commence_date,
    resale_price,
    -- New derived column
    SAFE_DIVIDE(resale_price, CAST(floor_area_sqm AS NUMERIC)) AS price_per_sqm
FROM {{ source('resale_flat', 'resale_prices') }}

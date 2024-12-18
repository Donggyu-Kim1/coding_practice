WITH RankedData AS (
    SELECT 
        ID,
        SIZE_OF_COLONY,
        PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) * 100 AS percentile
    FROM ECOLI_DATA
),
QuartileData AS (
    SELECT
        ID,
        SIZE_OF_COLONY,
        CASE
            WHEN percentile <= 25 THEN 'CRITICAL'
            WHEN percentile <= 50 THEN 'HIGH'
            WHEN percentile <= 75 THEN 'MEDIUM'
            ELSE 'LOW'
        END AS COLONY_NAME
    FROM RankedData
)
SELECT ID, COLONY_NAME
FROM QuartileData
ORDER BY ID ASC;
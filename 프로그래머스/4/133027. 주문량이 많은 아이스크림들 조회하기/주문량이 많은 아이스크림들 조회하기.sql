WITH JULY_ORDER AS (
    SELECT 
        FLAVOR,
        SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY J
    GROUP BY FLAVOR
),
FIRST_JULY AS (
    SELECT
        H.FLAVOR,
        H.TOTAL_ORDER + J.TOTAL_ORDER AS TOTAL_ORDER
    FROM JULY_ORDER J
    JOIN FIRST_HALF H ON J.FLAVOR = H.FLAVOR
    ORDER BY TOTAL_ORDER DESC
)
SELECT FLAVOR FROM FIRST_JULY
LIMIT 3
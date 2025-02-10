WITH GRADE_INFO AS (
    SELECT 
        e.EMP_NO,
        e.EMP_NAME,
        CASE 
            WHEN AVG(g.SCORE) >= 96 THEN 'S'
            WHEN AVG(g.SCORE) >= 90 THEN 'A'
            WHEN AVG(g.SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_GRADE g
    JOIN HR_EMPLOYEES e ON g.EMP_NO = e.EMP_NO
    GROUP BY e.EMP_NO
    ORDER BY e.EMP_NO ASC
)
SELECT 
    g.EMP_NO,
    g.EMP_NAME,
    g.GRADE,
    CASE
        WHEN GRADE = 'S' THEN e.SAL * 0.2
        WHEN GRADE = 'A' THEN e.SAL * 0.15
        WHEN GRADE = 'B' THEN e.SAL * 0.10
        ELSE 0
    END AS BONUS
FROM GRADE_INFO g
JOIN HR_EMPLOYEES e ON g.EMP_NO = e.EMP_NO
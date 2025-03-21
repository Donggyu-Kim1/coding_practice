WITH Front_End AS (
    SELECT
        SUM(CODE) AS CODE
    FROM SKILLCODES 
    GROUP BY CATEGORY
    HAVING CATEGORY = 'Front End'
),
Python AS (
    SELECT
        CODE
    FROM SKILLCODES
    WHERE NAME = 'Python'
),
C_SHARP AS (
    SELECT
        CODE
    FROM SKILLCODES
    WHERE NAME = 'C#'
),
GRADE_INFO AS (
    SELECT 
        CASE 
            WHEN (F.CODE & D.SKILL_CODE > 0) AND (P.CODE & D.SKILL_CODE > 0) THEN 'A'
            WHEN (C.CODE & D.SKILL_CODE > 0) THEN 'B'
            WHEN (F.CODE & D.SKILL_CODE > 0) THEN 'C'
        END AS GRADE,
        D.ID,
        D.EMAIL
    FROM DEVELOPERS D, Front_End F, Python P,C_SHARP C
)
SELECT * FROM GRADE_INFO
WHERE GRADE IS NOT NULL
ORDER BY GRADE ASC, ID ASC;
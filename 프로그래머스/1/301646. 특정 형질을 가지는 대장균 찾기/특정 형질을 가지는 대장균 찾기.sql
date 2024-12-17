SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE 
    (GENOTYPE & 2) = 0    -- 2번째 비트가 0
    AND (
        (GENOTYPE & 1) = 1    -- 1번째 비트가 1
        OR (GENOTYPE & 4) = 4  -- 3번째 비트가 1
    );
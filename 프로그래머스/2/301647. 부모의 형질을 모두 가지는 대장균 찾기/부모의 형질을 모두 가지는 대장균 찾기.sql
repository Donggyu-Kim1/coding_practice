SELECT 
    C.ID AS ID,
    C.GENOTYPE AS GENOTYPE,
    E.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA E
LEFT JOIN ECOLI_DATA C ON E.ID = C.PARENT_ID
WHERE 
    C.ID IS NOT NULL AND
    (C.GENOTYPE & E.GENOTYPE) = E.GENOTYPE
ORDER BY ID;

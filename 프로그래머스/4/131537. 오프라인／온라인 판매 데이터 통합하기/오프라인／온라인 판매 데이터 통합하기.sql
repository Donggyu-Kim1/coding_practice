SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM (
    SELECT 
        DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
        PRODUCT_ID,
        USER_ID,
        SALES_AMOUNT
    FROM ONLINE_SALE
    WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03'
    
    UNION ALL
    
    SELECT 
        DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
        PRODUCT_ID,
        NULL as USER_ID,
        SALES_AMOUNT
    FROM OFFLINE_SALE
    WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03'
) AS COMBINED_SALES
ORDER BY 
    SALES_DATE ASC,
    PRODUCT_ID ASC,
    USER_ID ASC;

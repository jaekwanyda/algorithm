-- 코드를 입력하세요
SELECT WAREHOUSE_ID
        , WAREHOUSE_NAME
        , ADDRESS
        , CASE WHEN ISNULL(FREEZER_YN) THEN 'N'
        ELSE FREEZER_YN END AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE SUBSTR(ADDRESS,1,3) = '경기도'
ORDER BY WAREHOUSE_ID
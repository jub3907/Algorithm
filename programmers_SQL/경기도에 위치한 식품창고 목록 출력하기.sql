-- 코드를 입력하세요
SELECT warehouse_id
    , warehouse_name
    , address
    , CASE WHEN freezer_yn is null then 'N'
           ELSE freezer_yn
      END as FREEZER_YN
FROM FOOD_WAREHOUSE F
WHERE F.address LIKE '%경기도%'
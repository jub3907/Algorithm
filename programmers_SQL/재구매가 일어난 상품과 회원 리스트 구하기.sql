-- 코드를 입력하세요
select USER_ID, PRODUCT_ID
from (
    SELECT user_id, product_id, count(*) as cnt
    from online_sale
    group by user_ID, product_id
)
where cnt > 1
order by user_id, product_id desc
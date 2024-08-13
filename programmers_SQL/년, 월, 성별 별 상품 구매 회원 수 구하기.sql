-- 코드를 입력하세요to_char
SELECT EXTRACT (year from online_sale.sales_date) as YEAR
    , EXTRACT (month from online_sale.sales_date) as MONTH
    , user_info.gender as GENDER
    , count(distinct user_info.user_id) as users
from online_sale inner join user_info 
on online_sale.user_id = user_info.user_id
where user_info.gender is not null
group by EXTRACT(year from online_sale.sales_date)
        , EXTRACT(month from online_sale.sales_date)
        , user_info.gender
order by YEAR, MONTH, GENDER

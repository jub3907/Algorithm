-- 코드를 입력하세요
SELECT A.category , sum(B.sales) as TOTAL_SALES
from book A
inner join book_sales B
on A.book_id = B.book_id
where to_char(B.sales_date, 'YYYY-MM') = '2022-01'
group by A.category
order by A.category
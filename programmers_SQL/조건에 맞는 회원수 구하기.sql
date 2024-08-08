-- 코드를 입력하세요
SELECT sum(count(user_id)) as USERS
from user_info
where to_char(user_info.joined, 'YYYY') = '2021' and (user_info.age between 20 and 29)
group by user_info.user_id
-- 코드를 입력하세요
select count(A.count) as count
from (
    SELECT count(animal_ins.name) as count
    from animal_ins
    where animal_ins.name is not null
    group by animal_ins.name
) A


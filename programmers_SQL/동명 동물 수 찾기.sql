-- 코드를 입력하세
select *
from (
        SELECT animal_ins.name, count(animal_ins.name) as count
        from animal_ins
        group by animal_ins.name
    ) A
where A.count > 1
order by A.name
;
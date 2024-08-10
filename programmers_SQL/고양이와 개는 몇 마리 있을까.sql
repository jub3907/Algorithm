-- 코드를 입력하세요
SELECT animal_ins.animal_type, count(animal_ins.animal_type)
from animal_ins
group by animal_ins.animal_type
order by animal_ins.animal_type
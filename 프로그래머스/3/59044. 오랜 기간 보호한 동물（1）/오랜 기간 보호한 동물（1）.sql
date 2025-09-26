select 
    NAME,
    DATETIME
from
    animal_ins as t3
where
    not exists (
    SELECT
        t1.animal_id
    from
        animal_ins as t1
    JOIN
        animal_outs as t2 on t1.animal_id=t2.animal_id
    where t1.animal_id=t3.animal_id
)
order by datetime asc
limit 3
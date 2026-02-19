select 
    ins.ANIMAL_ID, ins.NAME
from
    ANIMAL_INS as ins,
    ANIMAL_OUTS as outs
where
    ins.animal_id = outs.animal_id    
order by
    (outs.datetime - ins.datetime) desc
limit 2
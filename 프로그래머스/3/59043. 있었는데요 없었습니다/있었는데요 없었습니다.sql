SELECT
    t1.ANIMAL_ID,
    t1.NAME
FROM
    ANIMAL_INS as t1
JOIN
    ANIMAL_OUTS as t2 on t1.animal_id=t2.animal_id
where
    t1.DATETIME>t2.DATETIME
order by t1.datetime asc
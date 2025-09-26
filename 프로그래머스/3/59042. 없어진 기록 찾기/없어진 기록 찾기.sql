SELECT
    t2.ANIMAL_ID,
    t2.NAME
FROM
    ANIMAL_OUTS as t2
WHERE
    NOT EXISTS (
        SELECT
            t1.ANIMAL_ID
        FROM
            ANIMAL_INS as t1
        where t1.animal_id=t2.animal_id
    )
order by t2.animal_id
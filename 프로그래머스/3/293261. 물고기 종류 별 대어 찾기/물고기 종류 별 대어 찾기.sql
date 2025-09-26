WITH ranked as (
    SELECT
        t1.ID,
        t2.FISH_NAME,
        t1.LENGTH,
        RANK() OVER
            (PARTITION BY t1.FISH_TYPE
            ORDER BY t1.LENGTH desc) as rnk
    FROM
        FISH_INFO as t1
    JOIN
        FISH_NAME_INFO as t2 ON t1.FISH_TYPE=t2.FISH_TYPE
)
SELECT
    ID,FISH_NAME,LENGTH
FROM
    ranked
WHERE
    rnk=1
ORDER BY
    ID ASC
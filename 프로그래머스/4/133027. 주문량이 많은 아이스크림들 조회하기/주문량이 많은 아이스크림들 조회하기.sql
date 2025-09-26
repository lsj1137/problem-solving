SELECT FLAVOR
from
    (SELECT 
        FLAVOR,
        TOTAL_ORDER
    from
        FIRST_HALF
    union
    (SELECT
        FLAVOR,
        sum(total_order) as TOTAL_ORDER
    from JULY
    group by flavor)
    ) as total
group by flavor
order by sum(TOTAL_ORDER) desc
LIMIT 3
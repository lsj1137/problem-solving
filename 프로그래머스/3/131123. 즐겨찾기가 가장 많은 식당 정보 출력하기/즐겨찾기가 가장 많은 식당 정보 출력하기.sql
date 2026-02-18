# select * from rest_info order by favorites desc

select
    FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from
    REST_INFO
where
    (FOOD_TYPE, FAVORITES) in (select
        FOOD_TYPE, MAX(FAVORITES) as MAX_FAVORITES
    from
        REST_INFO
    group by
        FOOD_TYPE) 
order by
    food_type desc
select
    ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") as OUT_DATE,
    CASE 
        WHEN OUT_DATE is NULL
        THEN '출고미정'
        WHEN OUT_DATE <= '2022-05-01'
        THEN '출고완료'
        ELSE '출고대기'
    END
        as 출고여부
from
    FOOD_ORDER
order by
    order_id asc
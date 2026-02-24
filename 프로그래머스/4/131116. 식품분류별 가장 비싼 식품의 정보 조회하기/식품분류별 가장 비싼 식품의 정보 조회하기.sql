-- 코드를 입력하세요
SELECT FOOD_PRODUCT.CATEGORY, MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT,
    (
        select CATEGORY, max(price) as max_price
        from food_product
        group by category
    ) as max_price_per_category
where
    FOOD_PRODUCT.category in ('과자', '국', '김치', '식용유')
    and 
    (FOOD_PRODUCT.category, FOOD_PRODUCT.price) = (max_price_per_category.category, max_price_per_category.max_price)
order by
    price desc
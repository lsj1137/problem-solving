-- 코드를 입력하세요
SELECT PRODUCT_CODE, SUM(price*sales_amount) SALES from PRODUCT join OFFLINE_SALE on PRODUCT.product_id=OFFLINE_SALE.product_id group by product_code order by SALES desc, PRODUCT_CODE asc
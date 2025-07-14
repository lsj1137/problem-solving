-- 코드를 입력하세요
SELECT FLAVOR from FIRST_HALF where FLAVOR in (SELECT FLAVOR from ICECREAM_INFO where INGREDIENT_TYPE='fruit_based') and TOTAL_ORDER>3000 group by flavor
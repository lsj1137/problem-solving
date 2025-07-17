-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) as count from ANIMAL_INS where ANIMAL_TYPE='Cat' or ANIMAL_TYPE='Dog' Group by animal_type order by ANIMAL_TYPE
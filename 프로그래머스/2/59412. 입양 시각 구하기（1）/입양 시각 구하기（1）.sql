-- 코드를 입력하세요
SELECT hour(DATETIME) as HOUR, COUNT(hour(DATETIME)) as COUNT from ANIMAL_OUTS where hour(DATETIME)>8 and hour(datetime)<20 group by hour(DATETIME) order by hour(DATETIME)
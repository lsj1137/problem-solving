-- 코드를 작성해주세요
select COUNT(ID) as FISH_COUNT, month(TIME) as MONTH from FISH_INFO group by MONTH order by MONTH
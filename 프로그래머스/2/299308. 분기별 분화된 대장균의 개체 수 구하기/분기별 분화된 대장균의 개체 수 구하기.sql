-- 코드를 작성해주세요
select concat(quarter(DIFFERENTIATION_DATE),'Q') as QUARTER, COUNT(*) as ECOLI_COUNT from ECOLI_DATA group by QUARTER order by quarter asc
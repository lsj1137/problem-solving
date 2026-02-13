select
dept.DEPT_ID, dept.DEPT_NAME_EN, ROUND(AVG(emp.SAL),0) as AVG_SAL
from
HR_DEPARTMENT dept,
HR_EMPLOYEES emp
where
dept.dept_id = emp.dept_id
group by
dept_id
order by
avg_sal desc
-- 코드를 작성해주세요
select
    e.EMP_NO, EMP_NAME, final_grade.grade,
    case 
    when final_grade.grade='S'
    then sal * 0.2
    when final_grade.grade='A'
    then sal * 0.15
    when final_grade.grade = 'B'
    then sal * 0.1
    else 0
    end as BONUS
from
    HR_EMPLOYEES as e,
    (select
        emp_no,
        case 
        when AVG_SCORE >= 96
        then 'S'
        when AVG_SCORE >= 90
        then 'A'
        when AVG_SCORE >=80
        then 'B'
        else 'C'
        end as GRADE
    from 
        (select emp_no, avg(score) as AVG_SCORE
        from HR_GRADE
        group by emp_no
        ) as avg_grade
    ) as final_grade
where e.emp_no = final_grade.emp_no
order by
    emp_no asc

    
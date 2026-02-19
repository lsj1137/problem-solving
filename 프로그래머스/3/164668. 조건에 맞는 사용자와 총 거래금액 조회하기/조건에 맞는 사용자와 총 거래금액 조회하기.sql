select
    b.writer_id as USER_ID, u.NICKNAME, sum(b.price) as TOTAL_SALES
from
    USED_GOODS_BOARD as b,
    USED_GOODS_USER  as u
where 
    status = 'DONE'
    and
    b.writer_id = u.user_id
group by
    writer_id
having
    total_sales>=700000
order by
    total_sales asc
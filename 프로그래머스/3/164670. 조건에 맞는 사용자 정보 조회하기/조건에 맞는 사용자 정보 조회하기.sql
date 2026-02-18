SELECT
    u.USER_ID,
    u.NICKNAME,
    CONCAT(u.city, ' ', u.street_address1, ' ', u.street_address2) as 전체주소,
    concat(substr(u.tlno, 1, 3),'-',substr(u.tlno, 4, 4),'-',substr(u.tlno, 8, 4)) as 전화번호
FROM
    USED_GOODS_BOARD as b,
    USED_GOODS_USER as u
where
    b.writer_id = u.user_id
group by
    u.user_id
having
    count(u.user_id) > 2
order by
    u.user_id desc
SELECT *
from places
where 
HOST_ID in (SELECT HOST_ID from
(SELECT HOST_ID, COUNT(ID) as cnt
from places
group by HOST_ID) t1
where t1.cnt>1)
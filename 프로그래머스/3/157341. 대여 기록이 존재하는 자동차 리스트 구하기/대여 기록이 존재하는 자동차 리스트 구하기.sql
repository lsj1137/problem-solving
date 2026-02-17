select distinct
    CAR_RENTAL_COMPANY_CAR.CAR_ID
from 
    CAR_RENTAL_COMPANY_CAR,
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
where
    CAR_RENTAL_COMPANY_CAR.car_id = CAR_RENTAL_COMPANY_RENTAL_HISTORY.car_id
    and
    start_date like "%-10-%"
    and 
    car_type='세단'
order by
    CAR_RENTAL_COMPANY_CAR.car_id desc
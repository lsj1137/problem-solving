SELECT 
    CATEGORY,
    sum(book_sales.sales) as TOTAL_SALES
from
    book,
    book_sales
where
    book.book_id = book_sales.book_id
    and
    book_sales.sales_date like '2022-01-%'
group by
    category
order by
    category asc
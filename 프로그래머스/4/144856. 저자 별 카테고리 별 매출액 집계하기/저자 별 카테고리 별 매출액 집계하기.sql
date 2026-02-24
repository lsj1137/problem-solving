# select
#     a.author_id as AUTHOR_ID, AUTHOR_NAME, CATEGORY, final_sales.total_sales_per_category
# from
#     author as a,
#     (select category, sum(total_sales_per_book) as total_sales_per_category
#     from (
#         select b.book_id, category, price * sum(sales) as total_sales_per_book
#         from
#             book as b,
#             book_sales as bs
#         where
#             b.book_id = bs.book_id
#             and 
#             bs.sales_date>="2022-01-01" and bs.sales_date<"2022-02-01"
#         group by
#             b.book_id) as sales_per_book
#     group by
#         category) as final_sales
# where
#     bs.sales_date>="2022-01-01" and bs.sales_date<"2022-02-01"
#     and
#     a.author_id = b.author_id
# group by
#     author_id, category
# order by
#     author_id asc, category desc

select a.AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(total_sales_per_book) as TOTAL_SALES
from 
    author as a,
    (select author_id, b.book_id, category, price * sum(sales) as total_sales_per_book
    from
        book as b,
        book_sales as bs
    where
        b.book_id = bs.book_id
        and 
        bs.sales_date>="2022-01-01" and bs.sales_date<"2022-02-01"
    group by
        b.book_id) as sales_per_book
where
    a.author_id=sales_per_book.author_id
group by
    a.author_id, category
order by
    author_id asc, category desc


SELECT
concat('/home/grep/src/', b.board_id, '/', file_id, file_name, file_ext) as FILE_PATH
from
USED_GOODS_BOARD as b,
USED_GOODS_FILE  as f
where
b.board_id = f.board_id
and
b.views = (select
max(views) max_view
from used_goods_board)
order by
file_id desc
sh,sm,ss = map(int,input().split(":"))
fh,fm,fs = map(int,input().split(":"))
if sh>fh:
    h = 24-sh+fh
else:
    h = fh-sh
if sm>fm:
    if h>0:
        h -= 1
    else:
        h += 23
    m = 60-sm+fm
else:
    m = fm-sm
if ss>fs:
    if m>0:
        m -= 1
    else:
        if h>0:
            h -= 1
            m += 59
        else:
            h += 23
            m += 59
    s = 60-ss+fs
else:
    s = fs-ss
r = h*3600 + m*60 + s
print(r)
#this one on python2
k = ["key 1","key 2","key 3","key 4"]
v = [x for x in range(1, 7)]

def function(k, v):
    if len(k) > len(v):
        c = map(None, k, v)
    else:
        c = zip(k, v)
    return dict(c)

print 'List 1',function(k, v)
print 'List 2',function(v, k)
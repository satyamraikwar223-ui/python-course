def my_generator():
    for i in range(10):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

#genetor use in other way

for j in gen:
    print(j)

#benefits of usnig generator
#Python generators optimize memory and performance by producing 
#data on the fly using the yield keyword instead of loading entire sequences into RAM at once.
# This "lazy evaluation" model provides major efficiency gains,
#  especially when processing vast or streaming datasets.
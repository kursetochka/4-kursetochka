from matplotlib import pyplot
with open('C:/Users/User/Downloads/result.csv') as f: 
    lines = f.readlines()[1:]  
    c1 = [] 
    c2 = [] 
    values = []
for line in lines: 
    row = line.strip().split(',')
    c1.append(float(row[0]))
    c2.append(float(row[1]))
    values.append(float(row[2]))
min_value = min(values) 
max_value = max(values)
min_index = values.index(min_value) 
max_index = values.index(max_value)
fig = pyplot.figure() 
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(c1, c2, values)
ax.plot( [c1[min_index]], [c2[min_index]], [min_value], 'ro' )
ax.plot( [c1[max_index]], [c2[max_index]], [max_value], 'go' )
ax.set_xlabel('c1') 
ax.set_ylabel('c2') 
ax.set_zlabel('f(c)')
pyplot.savefig('C:/Users/User/Downloads/result.png')
pyplot.show()

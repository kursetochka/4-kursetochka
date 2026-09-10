data = csvread('C:/Users/User/Downloads/result_octave.csv', 1, 0);

c1 = data(:, 1);
c2 = data(:, 2);
values = data(:, 3);

[min_value, min_index] = min(values);
[max_value, max_index] = max(values);

x = reshape(c1, 25, 25);
y = reshape(c2, 25, 25);
z = reshape(values, 25, 25);

surf(x, y, z);

hold on;

plot3(c1(min_index), c2(min_index), min_value, 'ro');
plot3(c1(max_index), c2(max_index), max_value, 'go');

xlabel('c1');
ylabel('c2');
zlabel('f(c)');

print('C:/Users/User/Downloads/result.png', '-dpng');

hold off;

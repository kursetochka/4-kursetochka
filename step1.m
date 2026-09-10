A = csvread('C:/Users/User/Downloads/matA.csv');
b = csvread('C:/Users/User/Downloads/matb.csv');
function value = func(c1, c2, A, b)
  x1 = 1;
  x2 = -1;
  h = 0.001;
  for i = 1:10000
    u = c1 * x1 + c2 * x2;
    dx1 = A(1,1) * x1 + A(1,2) * x2 + b(1) * u;
    dx2 = A(2,1) * x1 + A(2,2) * x2 + b(2) * u;
    x1 = x1 + h * dx1;
    x2 = x2 + h * dx2;
  endfor
  value = (x1 ^ 2 + x2 ^ 2) / 2;
endfunction
c_values = [];
step = 2 / 24;
for i = 0:24
  c_values(end + 1) = -1 + i * step;
endfor
f = fopen('C:/Users/User/Downloads/result_octave.csv', 'w');
fprintf(f, 'c1,c2,f\n');
for i = 1:length(c_values)
  for j = 1:length(c_values)
    c1 = c_values(i);
    c2 = c_values(j);
    value = func(c1, c2, A, b);
    fprintf(f, '%f,%f,%f\n', c1, c2, value);
  endfor
endfor
fclose(f);

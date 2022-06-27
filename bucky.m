% Code Matlab mo phong he dong thuan voi do thi G1
A=zeros(60,60);
 for i=1:59
  A(i,i+1)=1;
  A(i+1,i)=1;
 end
A(60,1)=1;
A(1,60)=1;
G = graph(A);
 global L
 L=laplacian(G)*eye(60);

 % Giai phuong trinh vi phan dung ode45
x0 = 10*(rand(60,1)-0.5); % Dieu kien dau
 [t,x] = ode45(@control_law,[0 100],x0);

 % Bieu dien tren do thi
 figure(2);hold on;
 for i=1:60
 plot(t,x(:,i)','LineWidth',1);
 end
xlabel 'Thoi gian [s]';
ylabel 'Bien trang thai x_i(t)';
 title 'x_i(t)'
 box on;

%% Ham tinh luat dong thuan
 function dpdt = control_law(t,p)
 global L
 dpdt = -L*p;
 end
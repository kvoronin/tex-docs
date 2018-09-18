%% 1. Laplace, feorder 0
%% 1.1 Uniform refinement
%%dofs
%n_ur = 3;
%X_ur = zeros(n_ur,1);
%X_ur(1) = 8231;
%X_ur(2) = 63677;
%X_ur(3) = 501049;
%
%%sigma errors
%Y_ur = zeros(n_ur,1);
%Y_ur(1) = 0.113;
%Y_ur(2) = 0.073;
%Y_ur(3) = 0.047;
%
%% reference line for order 0.5
%Y_order = zeros(n_ur,1);
%Y_order(1) = Y_ur(1);
%for i = 2 : n_ur
%  Y_order(i) = Y_order(i-1) * (X_ur(i-1) / X_ur(i))^0.5;
%end
%
%% 1.2 AMR
%n_amr = 5;
%%dofs
%X_amr = zeros(n_amr,1);
%X_amr(1) = 8231;
%X_amr(2) = 12421;
%X_amr(3) = 24068;
%X_amr(4) = 50849;
%X_amr(5) = 76852;
%
%%sigma errors
%Y_amr = zeros(n_amr,1);
%Y_amr(1) = 0.113;
%Y_amr(2) = 0.082;
%Y_amr(3) = 0.066;
%Y_amr(4) = 0.055;
%Y_amr(5) = 0.05;
%
%% 1.3 Plotting
%figure
%h = loglog(X_ur, Y_ur, '-x', 'linewidth', 2, 'markersize', 8, ...
%           X_amr, Y_amr, 'markersize', 8, '-o', 'linewidth', 2, ...
%           X_ur, Y_order,'--');
%set(gca(),"ydir","reverse");
%set(gca(),"xlabel","#dofs, log scale");
%set(gca(),"ylabel","error, reversed log scale");
%set(gcf(),"name","Laplace, f.e. order 0");

%% 2. Laplace, feorder 1
%% 2.1 Uniform refinement
%%dofs
%n_ur = 3;
%X_ur = zeros(n_ur,1);
%X_ur(1) = 4803;
%X_ur(2) = 36589;
%X_ur(3) = 285689;
%
%%sigma errors
%Y_ur = zeros(n_ur,1);
%Y_ur(1) = 0.064;
%Y_ur(2) = 0.041;
%Y_ur(3) = 0.026;
%
%%u errors
%Y_ur_u = zeros(n_ur,1);
%Y_ur_u(1) = 0.013;
%Y_ur_u(2) = 0.0041;
%Y_ur_u(3) = 0.0014;
%
%
%% reference line for order 0.5
%Y_order = zeros(n_ur,1);
%Y_order(1) = Y_ur(1);
%for i = 2 : n_ur
%  Y_order(i) = Y_order(i-1) * (X_ur(i-1) / X_ur(i))^0.5;
%end
%
%Y_order_u = zeros(n_ur,1);
%Y_order_u(1) = Y_ur(1);
%for i = 2 : n_ur
%  Y_order_u(i) = Y_order_u(i-1) * (X_ur(i-1) / X_ur(i))^1.0;
%end
%
%% 2.2 AMR
%n_amr = 5;
%%dofs
%X_amr = zeros(n_amr,1);
%X_amr(1) = 4803;
%X_amr(2) = 15371;
%X_amr(3) = 57767;
%X_amr(4) = 126099;
%X_amr(5) = 254799;
%
%%sigma errors
%Y_amr = zeros(n_amr,1);
%Y_amr(1) = 0.064;
%Y_amr(2) = 0.037;
%Y_amr(3) = 0.018;
%Y_amr(4) = 0.012;
%Y_amr(5) = 0.0079;
%
%%u errors
%Y_amr_u = zeros(n_amr,1);
%Y_amr_u(1) = 0.013;
%Y_amr_u(2) = 0.0034;
%Y_amr_u(3) = 0.00096;
%Y_amr_u(4) = 0.00059;
%Y_amr_u(5) = 0.00039;
%
%% 2.3 Plotting
%% sigma
%figure
%h = loglog(X_ur, Y_ur, '-x', 'linewidth', 2, 'markersize', 8, ...
%           X_amr, Y_amr, 'markersize', 8, '-o', 'linewidth', 2, ...
%           X_ur, Y_order,'--');
%set(gca(),"ydir","reverse");
%set(gca(),"xlabel","#dofs, log scale");
%set(gca(),"ylabel","error, reversed log scale");
%set(gcf(),"name","Laplace, f.e. order 1, sigma");
%
%%u
%figure
%h = loglog(X_ur, Y_ur_u, '-x', 'linewidth', 2, 'markersize', 8, ...
%           X_amr, Y_amr_u, 'markersize', 8, '-o', 'linewidth', 2, ...
%           X_ur, Y_order_u,'--');
%set(gca(),"ydir","reverse");
%set(gca(),"xlabel","#dofs, log scale");
%set(gca(),"ylabel","error, reversed log scale");
%set(gcf(),"name","Laplace, f.e. order 1, u");

%% 3. Transport, feorder 0
%% 3.1 Uniform refinement
%%dofs
%n_ur = 4;
%X_ur = zeros(n_ur,1);
%X_ur(1) = 1248;
%X_ur(2) = 9600;
%X_ur(3) = 75264;
%X_ur(4) = 595968;
%
%%sigma errors
%Y_ur = zeros(n_ur,1);
%Y_ur(1) = 0.96;
%Y_ur(2) = 0.99;
%Y_ur(3) = 0.75;
%Y_ur(4) = 0.57;
%
%% reference line for order 0.25
%Y_order = zeros(n_ur,1);
%Y_order(1) = Y_ur(1);
%for i = 2 : n_ur
%  Y_order(i) = Y_order(i-1) * (X_ur(i-1) / X_ur(i))^0.25;
%end
%
%% 3.2 AMR
%n_amr = 5;
%%dofs
%X_amr = zeros(n_amr,1);
%X_amr(1) = 1248;
%X_amr(2) = 3915;
%X_amr(3) = 11584;
%X_amr(4) = 28957;
%X_amr(5) = 55482;
%
%%sigma errors
%Y_amr = zeros(n_amr,1);
%Y_amr(1) = 0.96;
%Y_amr(2) = 0.85;
%Y_amr(3) = 0.77;
%Y_amr(4) = 0.65;
%Y_amr(5) = 0.59;
%
%% 3.3 Plotting
%figure
%h = loglog(X_ur, Y_ur, '-x', 'linewidth', 2, 'markersize', 8, ...
%           X_amr, Y_amr, 'markersize', 8, '-o', 'linewidth', 2, ...
%           X_ur, Y_order,'--');
%set(gca(),"ydir","reverse");
%set(gca(),"xlabel","#dofs, log scale");
%set(gca(),"ylabel","error, reversed log scale");
%set(gcf(),"name","Transport, f.e. order 0");

%% 4. Transport, feorder 1
%% 4.1 Uniform refinement
%%dofs
%n_ur = 3;
%X_ur = zeros(n_ur,1);
%X_ur(1) = 5280;
%X_ur(2) = 41088;
%X_ur(3) = 324096;
%
%%sigma errors
%Y_ur = zeros(n_ur,1);
%Y_ur(1) = 0.84;
%Y_ur(2) = 0.67;
%Y_ur(3) = 0.38;
%
%% reference line for order 0.5
%Y_order = zeros(n_ur,1);
%Y_order(1) = Y_ur(1);
%for i = 2 : n_ur
%  Y_order(i) = Y_order(i-1) * (X_ur(i-1) / X_ur(i))^0.5;
%end
%
%% 4.2 AMR
%n_amr = 5;
%%dofs
%X_amr = zeros(n_amr,1);
%X_amr(1) = 41088;
%X_amr(2) = 52459;
%X_amr(3) = 91007;
%X_amr(4) = 175670;
%X_amr(5) = 262318;
%
%%sigma errors
%Y_amr = zeros(n_amr,1);
%Y_amr(1) = 0.67;
%Y_amr(2) = 0.51;
%Y_amr(3) = 0.26;
%Y_amr(4) = 0.13;
%Y_amr(5) = 0.1;
%
%% 4.3 Plotting
%figure
%h = loglog(X_ur, Y_ur, '-x', 'linewidth', 2, 'markersize', 8, ...
%           X_amr, Y_amr, 'markersize', 8, '-o', 'linewidth', 2, ...
%           X_ur, Y_order,'--');
%set(gca(),"ydir","reverse");
%set(gca(),"xlabel","#dofs, log scale");
%set(gca(),"ylabel","error, reversed log scale");
%set(gcf(),"name","Transport, f.e. order 1");

% 5. Laplace, 4D
% 5.1 Uniform refinement
%dofs
n_ur = 3;
X_ur = zeros(n_ur,1);
X_ur(1) = 20889;
X_ur(2) = 318945;
X_ur(3) = 4986945;

%u errors
Y_ur_u = zeros(n_ur,1);
Y_ur_u(1) = 0.062;
Y_ur_u(2) = 0.023;
Y_ur_u(3) = 0.009;

%u errors
Y_ur_sigma = zeros(n_ur,1);
Y_ur_sigma(1) = 1.692;
Y_ur_sigma(2) = 1.024;
Y_ur_sigma(3) = 0.642;

% reference line for order 1.0
Y_order_u = zeros(n_ur,1);
Y_order_u(1) = Y_ur_u(1);
for i = 2 : n_ur
  Y_order_u(i) = Y_order_u(i-1) * (X_ur(i-1) / X_ur(i))^1.0;
end

% reference line for order 0.5
Y_order_sigma = zeros(n_ur,1);
Y_order_sigma(1) = Y_ur_sigma(1);
for i = 2 : n_ur
  Y_order_sigma(i) = Y_order_sigma(i-1) * (X_ur(i-1) / X_ur(i))^0.5;
end

% 5.2 AMR
n_amr = 6;
%dofs
X_amr = zeros(n_amr,1);
X_amr(1) = 20889;
X_amr(2) = 35622;
X_amr(3) = 90640;
X_amr(4) = 217764;
X_amr(5) = 409927;
X_amr(6) = 758146;

%u errors
Y_amr_u = zeros(n_amr,1);
Y_amr_u(1) = 0.062;
Y_amr_u(2) = 0.055;
Y_amr_u(3) = 0.033;
Y_amr_u(4) = 0.014;
Y_amr_u(5) = 0.0058;
Y_amr_u(6) = 0.0038;

%sigma errors
Y_amr_sigma = zeros(n_amr,1);
Y_amr_sigma(1) = 1.692;
Y_amr_sigma(2) = 1.519;
Y_amr_sigma(3) = 1.109;
Y_amr_sigma(4) = 0.751;
Y_amr_sigma(5) = 0.501;
Y_amr_sigma(6) = 0.418;

% 5.3 Plotting
figure
h = loglog(X_ur, Y_ur_u, '-x', 'linewidth', 2, 'markersize', 8, ...
           X_amr, Y_amr_u, 'markersize', 8, '-o', 'linewidth', 2, ...
           X_ur, Y_order_u,'--');
set(gca(),"ydir","reverse");
set(gca(),"xlabel","#dofs, log scale");
set(gca(),"ylabel","error, reversed log scale");
set(gcf(),"name","Laplace, 4d, u");

figure
h = loglog(X_ur, Y_ur_sigma, '-x', 'linewidth', 2, 'markersize', 8, ...
           X_amr, Y_amr_sigma, 'markersize', 8, '-o', 'linewidth', 2, ...
           X_ur, Y_order_sigma,'--');
set(gca(),"ydir","reverse");
set(gca(),"xlabel","#dofs, log scale");
set(gca(),"ylabel","error, reversed log scale");
set(gcf(),"name","Laplace, 4d, sigma");


%pause();
%close all;
%clear;

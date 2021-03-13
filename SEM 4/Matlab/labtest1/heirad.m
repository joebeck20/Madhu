function [radius,height] = heirad(equation,surface_area)
    syms r h;    
    S = solve(equation,surface_area == 2*pi*r^2 + 2*pi*r*h,r,h);
    radius = S.r;
    height = S.h;
end


%[r,h] = heirad('2*h -20*r ==0',100);
%fprintf('radius - %f\n height - %f\n',r(2),h(2))

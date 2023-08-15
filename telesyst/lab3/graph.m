clc;
close all;
clear all;

f=fopen('veloergometr 25-60-75-100-125 Wt, 50 obmin.txt');
c=fscanf(f,'%d');
a=zeros(length(c)/4,1);
for i=4:4:length(c)
    a(i/4)=c(i);
end
t=1:1:length(a);
figure;
plot(t,a);
xlabel('t, с');
ylabel('„——, уд/хв');
grid on;
fclose(f);

f=fopen('treadmill 3-4-5-6-7(run) kmh.txt');
c=fscanf(f,'%d');
a=zeros(length(c)/4,1);
for i=4:4:length(c)
    a(i/4)=c(i);
end
t=1:1:length(a);
figure;
plot(t,a);
xlabel('t, с');
ylabel('„——, уд/хв');
grid on;
fclose(f);
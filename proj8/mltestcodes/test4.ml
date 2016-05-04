
global int x;

function void foo1()
begin
    write("foo1: ",x,"\n");
    x := x + 10;
    write("foo1: ",x,"\n");
end

function void foo2()
begin
    write("foo2: ",x,"\n");
end

function void foo3()
begin
    int x := 300;
    write("foo3: ",x,"\n");
end

begin
    x = 0;
    write("main: ",x,"\n");
    foo1();
    write("main: ",x,"\n");
    foo1();
    write("main: ",x,"\n");
    foo2();
    write("main: ",x,"\n");
    foo3();
    write("main: ",x,"\n");
end

function void foo3(int ref x)
begin
    int y;
    write("foo3: ",ref x,"\n");
    read(y);
    ref x := ref x + y;
    write("foo3: ",ref x,"\n");
end

function void foo2(int ref x)
begin
    int z;
    read(z);
    ref x := ref x + z;
    write("foo2: ",ref x,"\n");
    foo3(ref x);
    write("foo3: ",ref x,"\n");
end

function void foo1(int ref x)
begin
    int t;
    read(t);
    write("foo1: ",ref x,"\n");
    ref x := t*ref x;
    write("foo1: ",ref x,"\n");
end

begin
    int ref x;
    read(ref x);
    write("main: ",ref x,"\n");
    foo1(ref x);
    write("main: ",ref x,"\n");
    
    foo2(ref x);
    write("main: ",ref x,"\n");
end

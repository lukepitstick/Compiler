function int foo1(int ref x,int ref y)
begin
    ref x := ref x + 1;
    write("foo1: ",ref x," ",ref y,"\n");
    ref y := ref y + 1;
    write("foo1: ",ref x," ",ref y,"\n");
    return ref x + ref y;
end

function int foo2(int ref x)
begin
    int b;
    read(b);
    int a;
	a := ref x;
    a := a + b;
    write("foo2: ",ref x," ",a,"\n");
end

begin
    int a;
    read(a);
    int b;
	b := foo1(a,a);
    write("main; ",a," ",b,"\n");
    
    int c;
    read(c);
    foo2(c);
end

function void foo()
begin
    int i := 0;
    i := i + 1;
    write("In foo: ",i,".\n");
end

function void foo2()
begin
    write("In foo2.\n");
end

begin
    write("In main.\n");
    ~foo();
    write("Returned to main.\n");
    ~foo();
    write("Returned to man. (Again.)\n");
    ~foo2();
    write("Returned to main.\n");
end

#begin
#  write("In main.\n");
#  write("In foo: 1\n");
#  write("Returned to main.\n");
 # write("In foo: 1\n");
 # write("Returned to main. (Again.)\n");
 # write("In foo2\n");
 # write("Returned to main.\n");
#end

function void foo()
begin
    int i;
    i := 0;
    while(i < 5)
    begin
        if(i % 2 == 0)
        begin
            write(i," ");
        end
        i := i + 1;
    end
    write("\n");
end


begin
    foo();
    write("Done\n");
    foo();
    write("Done\n");
end

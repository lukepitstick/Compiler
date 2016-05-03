
function int foo1()
begin
    return 10;
end

function string foo2()
begin
    return "Winter is coming.\n";
end

function string foo3()
begin
    int x;
    read(x);
    if(x >= 10)
    begin
        return "Yes\n";
    end
    else
    begin
        return "No\n";
    end
end

function int foo4()
begin
    return True;
end

begin
  write(foo1(),"\n");
  write(5*foo1()+foo1(),"\n");
  write(foo2());
  write(foo3());
  if (foo4())
  begin
    write("Yes\n");
  end
end

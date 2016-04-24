begin
bool b;
b := True;
if b then
begin
write("First level");
if b then
begin
write("Second level");
if b then
begin
write("Thrid level");
if b then
begin
write("Fourth level");
write("Exit fourth level");
end
write("Exit third level");
end
write("Exit second level");
end
write("Exit first level");
end
write("The program ended successfully!@#%#!@^$@#^");
end

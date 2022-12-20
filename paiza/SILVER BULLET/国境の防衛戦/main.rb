N = gets.to_i
SN = []
N.times do |i|
  SN[i] = gets.split("//")
end

N.times do |j|
  if SN[j][0] != ""
    puts(SN[j][0])
  else
    puts("\n")
  end
end
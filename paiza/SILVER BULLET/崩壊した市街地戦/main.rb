N = gets.to_i
abN = []
N.times do
  ab = gets.split(' ').map(&:to_s)
  abN.push(ab)
end

N.times do |i|
  ab = abN[i][0].chars.map(&:to_i)
  if ab[0]+ab[1]+ab[2] == abN[i][1].to_i
    puts "Yes"
  elsif ab[0]*10+ab[1]+ab[2] == abN[i][1].to_i
    puts "Yes"
  elsif ab[0]+ab[1]*10+ab[2] == abN[i][1].to_i
    puts "Yes"
  else
    puts "No"
  end
end
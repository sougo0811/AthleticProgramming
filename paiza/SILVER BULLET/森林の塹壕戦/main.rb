N,T = gets.split(' ').map(&:to_i)
pxN = []
N.times.map do
  px = gets.split(' ').map(&:to_i)
  pxN.push(px)
end

exp = 0
while T != 0
  exp += pxN[T-1][1]
  T = pxN[T-1][0]
end

puts exp
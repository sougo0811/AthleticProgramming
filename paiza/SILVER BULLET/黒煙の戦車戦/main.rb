H, W, K = gets.split(' ').map(&:to_i)
amidas = []
H.times.map do
  amida = gets.chomp.split('')
  amidas.push(amida)
end

start = amidas[0].index(K.to_s)
np = start
(H-2).times.map do |i|
  while 0 < np && amidas[i+1][np-1] == "."
    np -= 1
    amidas[i+1][np] = "#"
  end
  while np < W && amidas[i+1][np+1] == "."
    np += 1
    amidas[i+1][np] = "#"
  end
end

puts amidas[H-1][np]
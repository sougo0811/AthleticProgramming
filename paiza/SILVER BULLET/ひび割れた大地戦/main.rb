H,W,X = gets.split(' ').map(&:to_i)
s_HW = [[]*W]
H.times do |i|
  s_HW[i] = gets.split(' ').map(&:to_i)
end

if 0 < X-1
  pin_min = X-2
elsif
  pin_min = X-1
end
if X-1 < W
  pin_max = X
elsif
  pin_max = X-1
end


pin_cnt = s_HW[0][X-1]
(H-1).times do |i|
  for j in pin_min..pin_max do
    pin_cnt += s_HW[i+1][j]
  end
  if 0 < pin_min
    pin_min -= 1
  end
  if pin_max < W-1
    pin_max += 1 
  end
end

puts pin_cnt
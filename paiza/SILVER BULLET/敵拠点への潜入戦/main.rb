S = gets.chomp.split('').map(&:to_i)
N = gets.to_i
xyN = []
N.times do
  xy = gets.split(' ').map(&:to_i)
  xyN.push(xy)
end

for i in 0..N-1 do
  for j in (xyN[i][0]-1)...xyN[i][1] do
    if S[j] == 0
      S[j] = 1
    else
      S[j] = 0
    end
  end
end

print(S.join)
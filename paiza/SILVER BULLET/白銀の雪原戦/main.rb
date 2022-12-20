N = gets.to_i
AN = [[]*N]
N.times do |i|
  AN[i] = gets.split(' ').map(&:to_i)
end

ans = []
N.times do |j|
  A = AN[j].permutation(6).to_a
  MS = 0
  (A.length).times do |k|
    xs = []
    ys = []
    x1 = A[k][0]
    x2 = A[k][1]
    x3 = A[k][2]
    y1 = A[k][3]
    y2 = A[k][4]
    y3 = A[k][5]
    xs = [(x1-x2).abs,(x2-x3).abs,(x3-x1).abs]
    ys = [(y1-y2).abs,(y2-y3).abs,(y3-y1).abs]
    a = ((xs[0]**2)+(ys[0]**2))**0.5
    b = ((xs[1]**2)+(ys[1]**2))**0.5
    c = ((xs[2]**2)+(ys[2]**2))**0.5
    s = (a+b+c)*0.5
    if s-a < 0 or s-b < 0 or s-c < 0
      S = 0
    else
      S = (s*(s-a)*(s-b)*(s-c))**0.5
    end
    if MS < S
      MS = S
    end
  end
  ans.push(MS.to_i)
end
#puts ans
puts ans.index(ans.max)+1


#↓簡潔コード
'''
def hypot(a,b)
  Math.hypot(a[0]-b[0],a[1]-b[1])
end
def f(a)
  x,y,z = a.each_slice(2).to_a
  a=hypot(x,y)
  b=hypot(y,z)
  c=hypot(z,x)
  s=(a+b+c)/2
  s*(s-a)*(s-b)*(s-c)
end
p (1..gets.to_i).each.max_by{
  gets.split.map(&:to_i).permutation.map(&method(:f)).max
}
'''
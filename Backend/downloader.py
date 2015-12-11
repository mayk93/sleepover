import pafy
v = pafy.new("https://www.youtube.com/watch?v=TNW9Kh2PRIk")
s = v.allstreams[len(v.allstreams)-1]
print s

print("Size is %s" % s.get_filesize())
filename = s.download()  # starts download

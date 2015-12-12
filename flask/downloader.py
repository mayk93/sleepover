import pafy

def download():
    v = pafy.new("https://www.youtube.com/watch?v=TNW9Kh2PRIk")
    s = v.allstreams[len(v.allstreams)-1]

    filename = s.download("test.mp4")  # starts download

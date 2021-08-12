from ImageProcessor import ImageProcessor as ip

def example_load():
    arr = ip.load("42AI.png")

    assert arr is not None

    ip.display(arr)

example_load()
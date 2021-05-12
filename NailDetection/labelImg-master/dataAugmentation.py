import Augmentor

f = Augmentor.Pipeline("./nail_voc2007/JPEGImages")
f.rotate90(probability=1.0)
# f.flip_left_right(probability=1.0)
# f.sample(75)
f.process()
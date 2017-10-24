lines = [] #String
line_index = 0

sampleN = 50
clusterN = 3

sample = []      # PVector
cluster = []     # int
prevCluster = [] # int

center = [] # PVector
key_pressed_sign = False

def setup():
    size (800, 800, P2D)
    for i in range(sampleN):
        sample.append(PVector(random(100, width - 100), random(100, height -100)))
    for i in range(clusterN):
        center.append(PVector(random(10, width-10), random(10, height - 10)))
        
    for i in range(sampleN):
        cluster.append(i % clusterN)
        prevCluster.append(-1)
    
    key_pressed_sign = False

def draw():
    background(0)
    global key_pressed_sign
    if key_pressed_sign is True:
        clustering()
        key_pressed_sign = False
    
    for i in range(sampleN):
        pushMatrix()
        if cluster[i] == 0:
            stroke(255, 0, 0)
        elif cluster[i] == 1:
            stroke(255, 255, 0)
        elif cluster[i] == 2:
            stroke(0, 255, 255)
            
        noFill()
        rect(sample[i].x, sample[i].y, 20, 20)
        popMatrix()

    for i in range(clusterN):
        pushMatrix()
        
        if i == 0:
            fill(255, 0, 0)
        elif i == 1:
            fill(255, 255, 0)
        elif i == 2:
            fill(0, 255, 255)
            
        noStroke()
        ellipse(center[i].x, center[i].y, 30, 30)
        popMatrix()
        
def clustering():
    e = False
    for i in range(sampleN):
        if prevCluster[i] != cluster[i]:
            e = True
            
    if e is True:
        for i in range(sampleN):
            prevCluster[i] = cluster[i]
        
        for i in range(sampleN):
            max_cluster = -1
            max_value = width * height
            
            for j in range(clusterN):
                if max_value > PVector.dist(sample[i], center[j]):
                    max_value = PVector.dist(sample[i], center[j])
                    max_cluster = j
                    
            cluster[i] = max_cluster
            
            for j in range(clusterN):
                cn = 0
                cx = 0
                cy = 0
                
                for i in range(sampleN):
                    if cluster[i] == j:
                        cx = cx + sample[i].x
                        cy = cy + sample[i].y
                        cn += 1
                        
                if cn != 0:
                    center[j].x = cx/cn
                    center[j].y = cy/cn

def keyPressed():
    global key_pressed_sign
    key_pressed_sign = True
    
# mySketch imageOutput
# img = []
# imgStr = []
# def setup():
#     size(640, 360)
#     for num in range(1, 10):
#         imgStr.append("pic0" + str(num) + ".jpg")
#         
#     for num in range(10, 61):
#         imgStr.append("pic" + str(num) + ".jpg")
#         
#     for num in range(60):
#         img.append(loadImage(imgStr[num])) 
#         
#     imageMode(CENTER)
# 
# def draw():
#     background(0, 102, 153)
#     
#     for y in range(6):
#         for x in range(10):
#             image(img[x+y*10], 32 + x*64, 30 + y*60, 64, 60)

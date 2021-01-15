import PyTouchBar as ptb
import tkinter
import cv2



# 2170x60



window = tkinter.Tk()

#
count = 0




ptb.prepare_tk_windows(window)
window.minsize(400, 400)
window.title("TBTESTS")

lbl = ptb.Label(window, text="Button")
lbl.pack()
label = ptb.TouchBarItems.Button(image='test.bmp', image_position=ptb.ImagePosition.left,
                                 image_scale=ptb.ImageScale.none)
space = ptb.TouchBarItems.Space.Flexible()
space2 = ptb.TouchBarItems.Space.Flexible()

ptb.set_touchbar([label])


def test_task():
    global count
    # print('do some stuff ' + str(count))
    count = count + 1
    img = cv2.imread('test_start.bmp')
    img = cv2.putText(img, 'this is a test: ' + str(count), (10, 34), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1)
    cv2.imwrite('test.bmp', img)
    label = ptb.TouchBarItems.Button(image='test.bmp', image_position=ptb.ImagePosition.left,
                                     image_scale=ptb.ImageScale.none)
    ptb.set_touchbar([label])
    ptb.reload_touchbar()
    window.after(1, test_task)

window.after(10, test_task)
window.mainloop()

# pygame.init()
# surface = pygame.display.set_mode((100,200))
# ptb.prepare_pygame()
# pygame.display.set_caption('Title')
#
# while True:
#   	for event in pygame.event.get():
# 		  if event.type == pygame.QUIT:
# 			  pygame.quit()
# 			  break

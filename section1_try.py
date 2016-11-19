import numpy as np
import cv2

## The readImage function takes a file path as argument and returns image in binary form.
def readImage(filePath):
	cap = cv2.imread(filePath,cv2.CV_LOAD_IMAGE_GRAYSCALE)
	(thresh, binaryImage) = cv2.threshold(cap, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	cv2.imshow('frame',binaryImage)
	return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
#def findNeighbours(img,row,column):
 #   neighbours = []
	    #############  Add your Code here   ###############


    ###################################################
  #  return neighbours

##  colourCell function takes 4 arguments:-
##            img - input image
##            row - row coordinates of cell to be coloured
##            column - column coordinates of cell to be coloured
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
def colourCell(img,row,column,colourVal):
    #############  Add your Code here   ###############
        def create_blank(width, height, rgb_color=(0,0,0)):
                """Create new image(numpy array) filled with certain color in RGB"""
                image = np.zeros((height, width, 3), np.uint8)
                color = tuple(reversed(rgb_color))
                image[:] = color
                return image
        width, height = img.shape;
        red = (255, 255, 255)
        colored_img = create_blank(width, height, rgb_color=red)
        colored_img[row*20:((row+1)*20)-1,column*20:((column+1)*20)-1]=[colourVal,colourVal,colourVal]
        res = cv2.bitwise_and(colored_img,colored_img, mask= img)
       # cap = cv2.imread(res,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        #(thresh, im_bw) = cv2.threshold(res, 151, 255, cv
        return res
##  Main function takes the filepath of image as input.
##  You are not allowed to change any code in this function.
def main(filePath):
	img = readImage(filePath)
	coords = [(0,0),(9,9)]
	string = ""
	for coordinate in coords:
		img = colourCell(img, coordinate[0], coordinate[1], 150)
	cv2.imshow('canvas', img)	
    
## Specify filepath of image here. The main function is called in this section.
if __name__ == '__main__':
	filePath = 'maze00.jpg'
	img = main(filePath)
	#print("tapan")
	cv2.waitKey(0)
	cv2.destroyAllWindows()

import cv2

blanks = cv2.imread("./images/Fill in the blanks empty sheet.jpg")
fills = cv2.imread("./images/Fill in the blanks answe1.jpeg")

if blanks is None or fills is None:
    print("Error: Could not read one or both images.")
else:
    # Check the shapes of the images
    print("Blanks shape:", blanks.shape)
    print("Fills shape:", fills.shape)

    # Resize the images (adjust target dimensions accordingly)
    blanks = cv2.resize(blanks, (612, 792))
    fills = cv2.resize(fills, (612, 792))

    # Perform image merging
    final_img = cv2.addWeighted(fills,0.9,blanks,0.1,0)

    # Display the final image
    cv2.imshow("filled", final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

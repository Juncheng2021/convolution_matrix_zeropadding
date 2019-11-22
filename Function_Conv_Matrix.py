def conv_matrix(matrix, kernel):
     """
     Perform the convolution of the matrix 
        with the kernel using zero padding
    # Arguments
        matrix: input matrix np.array of size `(N, M)`
        kernel: kernel of the convolution 
            np.array of size `(2p + 1, 2q + 1)`
    # Output
        the result of the convolution
        np.array of size `(N, M)`

    # Pericles 
    # Version 2
    # 22/11/2019
    """ 
    if len(kernel.shape) == 2: # Confirm that the Kernel has lenght 2

        m, n  = kernel.shape # capture the shape of the Kernel 
        y, x = matrix.shape # capture the shape of the Matrix
        if ((m % 2) == 0 and (n % 2) == 0): # Kernel need to be`(2p + 1, 2q + 1)`

            new_image = np.zeros((y,x)) 

            matrix = np.pad(matrix, # Zero padding 
            ((int((m-1)/2),int((m-1)/2)),(int((n-1)/2),int((n-1)/2))),
            # the amount of rows and cols to add is equal the size of the Kernel
            # -1 and divided by 2 
            mode='constant') # constant value == 0

            for i in range(y):
                for j in range(x):
                    new_image[i][j] = np.sum(matrix[i:i+m, j:j+n]*kernel)
            return new_image
    elif len(kernel.shape) == 1:
        return print("expect Kernel lenght 2 and receive lenght 1")
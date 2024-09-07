public class spiral {
    

    public static void main(String[] args) {
        
        int[][] matrix3 = { { 3, 2, 1, 7 },
					        { 9, 11, 5, 4 },
					        { 6, 0, 13, 17 },
					        { 7, 21, 14, 15 } };
      int i=0;
      int j=0;
    
    while (j<3) {
        System.out.print(matrix3[i][j]+" ");
    j++;
        
    }
    while (i<3) {
        System.out.print(matrix3[i][j]+" ");
        i++;
    }
    while (j>0) {
        System.out.print(matrix3[i][j]+" ");
        j--;
    }
    while (i>1) {
        System.out.print(matrix3[i][j]+" ");
        i--;
    }
     while (j<2) {
         System.out.print(matrix3[i][j]+" ");
         j++;
    }
    while (i<2) {
        System.out.print(matrix3[i][j]+" ");
        i++;
    }
    while (j>0) {
        System.out.print(matrix3[i][j]+" ");
        j--;
    }    
    }
        
}
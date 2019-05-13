package DataStructures;

public class ArrayOddEven {
    public static void main(String[] args) {
        System.out.println("===starting to segregate odd and even array elements.");
        int[] input={4,2,1,5,6,12,19,20};
        int[] output=new int[input.length];
        int startpos=0;
        int endpos=output.length-1;
        for(int i=0;i<input.length;i++){
            if(input[i]%2==0){
                output[startpos]=input[i];
                startpos++;
            }else{
                output[endpos]=input[i];
                endpos--;
            }
        }
        System.out.println("=====Print output array=====");
        for(int i=0;i<output.length;i++){
            System.out.println("Element at output["+i+"] is: "+output[i]);
        }

    }
}

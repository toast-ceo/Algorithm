import java.util.*;

class Main {
    public static void main(String[] arg){
        Scanner in = new Scanner(System.in);

        Double[] arr = new Double[1000];
        int num = in.nextInt();
        Double max = 0.0;
        int sum = 0;
        double result = 0;

        for (int i =0 ; i<num; i++){
            arr[i] = in.nextDouble();
        }

        for (int i= 0; i<num; i++ ){
            if (max < arr[i]){
                max = arr[i];
            }
            sum += arr[i];
        }

        result = sum*100/max/num;
        System.out.println(result);

    }
}